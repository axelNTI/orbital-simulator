import scipy.constants
import parse
import calculations
import pandas
import vis_pandas
import visualize

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


parse.parse_file("data.json")

objects = parse.objects()
iterations = parse.iterations()
time_resolution = parse.time_resolution()
initial_x_scale = parse.initial_scale_x()
initial_y_scale = parse.initial_scale_y()
window_size = parse.window_size()
interval = parse.vis_interval()


visualize.init(window_size, initial_x_scale, initial_y_scale)

for iteration in range(iterations // time_resolution):
    iterate(objects, time_resolution)

    # Display every 3600th iteration to speed up the visualization
    if interval != 0:
        if iteration % interval == 0:
            visualize.visualize_step(objects)
    else:
        visualize.visualize_step(objects)
