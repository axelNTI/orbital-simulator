import scipy.constants
import parse



# F = ma

# F = G * (m1*m2) / r^2

# Two dimensional plane
def calculate_gravitational_force(obj1, obj2):
    G = scipy.constants.gravitational_constant
    dx = obj2["position"][0] - obj1["position"][0]
    dy = obj2["position"][1] - obj1["position"][1]
    r_squared = dx**2 + dy**2
    r = r_squared ** 0.5
    if r == 0:
        return (0.0, 0.0)  # Avoid division by zero; no force if at same position

    F = G * (obj1["mass"] * obj2["mass"]) / r_squared
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
