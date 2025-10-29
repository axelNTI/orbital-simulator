import pygame
import parse
import calculations
import visualize
import argparse
import concurrent.futures
import graph

def iterate(objects: list[dict[str, int | float | list[int]]], step: float) -> None:
    def velocity_update():
        for item in objects:
            forces = []

            for other_item in filter(lambda x: x != item, objects):
                force = calculations.calculate_gravitational_force(item, other_item)
                forces.append(force)

            total_force = calculations.calculate_sum_of_forces(forces)
            acceleration = calculations.calculate_acceleration_from_force(total_force, item["mass"])
            item["velocity"] = calculations.calculate_velocity(item["velocity"], acceleration, step)
    
    if args.concurrent:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            velocity_update()
    else:
        velocity_update()
    
    for item in objects:
        item["position"] = calculations.calculate_new_position(item["position"], item["velocity"], step)

def pause_simulation():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key ==  pygame.K_SPACE:
                    return

def exit_with_parse_error(key: str, message: str):
    print(f"Couldn't parse a value for '{key}': {message}")
    exit()

parser = argparse.ArgumentParser("orbital-simulator")
parser.add_argument("-f", "--file", 
                    help = "Specify a file path to open", 
                    default = "data.json",
                    type = str
                    )

parser.add_argument("-c", "--concurrent", 
                    help = "Enable concurrent velocity calculations", 
                    default = False,
                    action = "store_true"
                    )

parser.add_argument("-l", "--labels", 
                    help = "Enable planetary labels", 
                    default = False,
                    action = "store_true"
                    )

parser.add_argument("-dg", "--disable-graph", 
                    help = "Disable the velocity graph",
                    default = False,
                    action = "store_true"
                    )

parser.add_argument("-dv", "--disable-visualization", 
                    help = "Disable the visualization",
                    default = False,
                    action = "store_true"
                    )
    
args = parser.parse_args()
if not parse.parse_file(args.file):
    print(f"Couldn't open file {args.file}!")
    exit()


objects = parse.objects()
if not objects:
    print("No objects found in data file!")
    exit()

iterations = parse.iterations()
if not iterations:
    exit_with_parse_error("iterations", "Must be a valid positive integer!")

time_resolution = parse.time_resolution()
if not iterations:
    exit_with_parse_error("time_resolution", "Must, if specified, be a valid positive integer!")

initial_x_scale = parse.initial_scale_x()
if not initial_x_scale:
    exit_with_parse_error("min_x' or 'max_x", "Must, if specified, be a valid float!")

initial_y_scale = parse.initial_scale_y()
if not initial_y_scale:
    exit_with_parse_error("min_y' or 'max_y", "Must, if specified, be a valid float!")

interval = parse.vis_interval()
if not interval:
    exit_with_parse_error("visualization_interval", "Must, if specified, be a valid positive integer!")

if not args.disable_visualization:
    window_size = parse.window_size()
    if not window_size:
        exit_with_parse_error("window_size", "Format must be \"window_size\": [x, y] where x and y are valid positive integers!")

    visualize.init(window_size, initial_x_scale, initial_y_scale)

if not args.disable_graph:
    graph.init(objects)

MAX_ITERATIONS = int(iterations // time_resolution)
for iteration in range(MAX_ITERATIONS):
    if not args.disable_visualization:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key ==  pygame.K_SPACE:
                    pause_simulation()

    iterate(objects, time_resolution)

    label = f"Iteration {iteration} of {MAX_ITERATIONS}"

    if interval == 0 or iteration % interval == 0:
        if not args.disable_visualization:
            visualize.visualize_step(objects, label, args.labels)
        if not args.disable_graph:
            graph.graph_step(objects, interval)
