import scipy.constants
import parse
import calculations
import pandas
import vis_pandas
import visualize

objects = parse.parse_file("data.json")

def iterate(objects, step):
    for item in objects:
        forces = []

        for other_item in filter(lambda x: x != item, objects):
            force = calculations.calculate_gravitational_force(item, other_item)
            forces.append(force)

        total_force = calculations.calculate_sum_of_forces(forces)
        acceleration = calculations.calculate_acceleration_from_force(total_force, item["mass"])
        item["velocity"] = calculations.calculate_velocity(item["velocity"], acceleration, step)
        item["position"] = calculations.calculate_new_position(item["position"], item["velocity"], step)

ITERATIONS = 2629743 * 6
TIME_STEP = 10

WINDOW_SIZE = (800, 600)
MAX_X = 390_000_000
MIN_X = -370_000_000
MAX_Y = 410_000_000
MIN_Y = -360_000_000

initial_x_scale = (MIN_X, MAX_X)
initial_y_scale = (MIN_Y, MAX_Y)
visualize.init(WINDOW_SIZE, initial_x_scale, initial_y_scale)

for iteration in range(ITERATIONS):
    iterate(objects, TIME_STEP)

    # Display every 3600th iteration to speed up the visualization
    if iteration % 3600 == 0: 
        visualize.visualize_step(objects)
