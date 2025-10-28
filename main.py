import parse
import calculations
import visualize
import argparse
import concurrent.futures

def iterate(objects, step):
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

parser = argparse.ArgumentParser("orbital-simulator")
parser.add_argument("-f", "--file", 
                    help = "Specify a file path to open", 
                    default = "data.json",
                    type = str
                    )

parser.add_argument("-c", "--concurrent", 
                    help = "Enable concurrent velocity calculations", 
                    default = False,
                    type = bool
                    )
    
args = parser.parse_args()
if not parse.parse_file(args.file):
    print(f"Couldn't open file {args.file}!")
    exit()


objects = parse.objects()
iterations = parse.iterations()
time_resolution = parse.time_resolution()
initial_x_scale = parse.initial_scale_x()
initial_y_scale = parse.initial_scale_y()
window_size = parse.window_size()
interval = parse.vis_interval()

visualize.init(window_size, initial_x_scale, initial_y_scale)

MAX_ITERATIONS = int(iterations // time_resolution)
for iteration in range(MAX_ITERATIONS):
    iterate(objects, time_resolution)

    label = f"Iteration {iteration} of {MAX_ITERATIONS}"

    if interval != 0:
        if iteration % interval == 0:
            visualize.visualize_step(objects, label)
    else:
        visualize.visualize_step(objects, label)
