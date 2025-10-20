import scipy.constants
import parse
import calculations
import pandas
import vis_pandas
import visualize

objects = parse.parse_file("data.json")

ITERATIONS = 2629743 * 12
TIME_STEP = 60

objs = []

simulations = []

for iteration in range(ITERATIONS // TIME_STEP):
    for item in objects:
        forces = []

        for other_item in filter(lambda x: x != item, objects):
            force = calculations.calculate_gravitational_force(item, other_item)
            forces.append(force)

        total_force = calculations.calculate_sum_of_forces(forces)
        acceleration = calculations.calculate_acceleration_from_force(total_force, item["mass"])
        item["velocity"] = calculations.calculate_velocity(item["velocity"], acceleration, 1)
        item["position"] = calculations.calculate_new_position(item["position"], item["velocity"])
        objs.append(dict(item))
    
    simulations.append([dict(o) for o in objs])

vis_pandas.view_table(filter(lambda o: o["name"] == "Earth", objs))

visualize.visualize_simulation(simulations)