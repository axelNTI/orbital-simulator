import scipy.constants
import parse
import calculations
import pandas
import vis_pandas

objects = parse.parse_file("data.json")

ITERATIONS = 100

objs = []

for iteration in range(ITERATIONS):
    for item in objects:
        forces = []

        for other_item in filter(lambda x: x != item, objects):
            force = calculations.calculate_gravitational_force(item, other_item)
            forces.append(force)

        total_force = calculations.calculate_sum_of_forces(forces)
        acceleration = calculations.calculate_acceleration_from_force(total_force, item["mass"])
        item["velocity"] = calculations.calculate_velocity(item["velocity"], acceleration)
        item["position"] = calculations.calculate_new_position(item["position"], item["velocity"])

        objs.append(item)
vis_pandas.view_table(objs)
