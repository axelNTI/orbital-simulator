import scipy.constants
import parse



# F = ma

# F = G * (m1*m2) / r^2

# Two dimensional plane
def calculate_gravitational_force(obj1, obj2):
    G = scipy.constants.gravitational_constant
    dx = obj2.position[0] - obj1.position[0]
    dy = obj2.position[1] - obj1.position[1]
    r_squared = dx**2 + dy**2
    r = r_squared ** 0.5
    if r == 0:
        return (0.0, 0.0)  # Avoid division by zero; no force if at same position
    
    F = G * (obj1.mass * obj2.mass) / r_squared
    Fx = F * dx / r
    Fy = F * dy / r
    
    return (Fx, Fy)

def calculate_sum_of_forces(forces):
    total_fx = sum(force[0] for force in forces)
    total_fy = sum(force[1] for force in forces)
    return (total_fx, total_fy)

def calculate_acceleration_from_force(force, mass):
    ax = force[0] / mass
    ay = force[1] / mass
    return (ax, ay)

def calculate_velocity(initial_velocity, acceleration):
    vx = initial_velocity[0] + acceleration[0]
    vy = initial_velocity[1] + acceleration[1]
    return (vx, vy)

def calculate_new_position(initial_position, velocity):
    x = initial_position[0] + velocity[0]
    y = initial_position[1] + velocity[1]
    return (x, y)


# Temporary test data

# obj1 = type('Obj', (object,), {'mass': 5.972e24, 'position': (0.0, 0.0), 'velocity': (0.0, 0.0)})  # Earth
# obj2 = type('Obj', (object,), {'mass': 7.348e22, 'position': (384400000.0, 0.0), 'velocity': (0.0, 1022)} )  # Moon
# obj3 = type('Obj', (object,), {'mass': 1000.0, 'position': (7000000.0, 0.0), 'velocity': (0.0, 7120)})  # Satellite


all_objects = parse.parse_file("data.json")

iterations = 100
for iteration in range(iterations):
    for item in all_objects:
        forces = []
        for other_item in filter(lambda x: x != item, all_objects):
            force = calculate_gravitational_force(item, other_item)
            forces.append(force)
        total_force = calculate_sum_of_forces(forces)
        print(f"Total gravitational force on object with mass {item.mass} kg: Fx = {total_force[0]} N, Fy = {total_force[1]} N")
        acceleration = calculate_acceleration_from_force(total_force, item.mass)
        print(f"Resulting acceleration: ax = {acceleration[0]} m/s², ay = {acceleration[1]} m/s²\n")
        item.velocity = calculate_velocity(item.velocity, acceleration)
        print(f"Updated velocity: vx = {item.velocity[0]} m/s, vy = {item.velocity[1]} m/s\n")
        item.position = calculate_new_position(item.position, item.velocity)
        print(f"Updated position: x = {item.position[0]} m, y = {item.position[1]} m\n")
    
