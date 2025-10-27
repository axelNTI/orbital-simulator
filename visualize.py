import pygame
import pygame.freetype
import copy

FONT_SIZE = 24

def init(size, initial_scale_x = (-1, 1), initial_scale_y = (-1, 1)):
    global window, window_size, clock, is_running, min_x, min_y, max_x, max_y, font
    pygame.init()
    font = pygame.freetype.Font(None, FONT_SIZE)

    # Set up the window
    window_size = size
    (min_x, max_x) = initial_scale_x
    (min_y, max_y) = initial_scale_y
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Orbital Simulation Visualization")

    clock = pygame.time.Clock()
    is_running = True

def visualize_step(step, label = ""):
    global min_x, max_x, min_y, max_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window.fill((0, 0, 0))  # Clear the screen with black

    # Draw each object
    for obj in step:
        tmp_obj = copy.deepcopy(obj)

        pos_x = tmp_obj["position"][0]
        pos_y = tmp_obj["position"][1]
        min_x = min(min_x, pos_x)
        min_y = min(min_y, pos_y)
        max_x = max(max_x, pos_x)
        max_y = max(max_y, pos_y)

        tmp_obj["position"] = (
            (tmp_obj["position"][0] - min_x) / (max_x - min_x) * window_size[0],
            (tmp_obj["position"][1] - min_y) / (max_y - min_y) * window_size[1]
        )
        x, y = int(tmp_obj["position"][0]), int(tmp_obj["position"][1])
        pygame.draw.circle(window, tmp_obj["color"], (tmp_obj["position"][0], tmp_obj["position"][1]), tmp_obj["radius"])

    if label != "":
        font.render_to(window, (20, 20), label, (255, 255, 255))

    pygame.display.flip()
    # pygame.time.wait(1)  # Pause for a short duration to visualize the step

def visualize_simulation(simulation):
    init()
    # Get max x and y for scaling
    max_x = max(obj["position"][0] for step in simulation for obj in step)
    max_y = max(obj["position"][1] for step in simulation for obj in step)
    min_x = min(obj["position"][0] for step in simulation for obj in step)
    min_y = min(obj["position"][1] for step in simulation for obj in step)

    print(f"Max X: {max_x}, Max Y: {max_y}, Min X: {min_x}, Min Y: {min_y}")

    simulation = simulation[::3600]

    for step in simulation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window.fill((0, 0, 0))  # Clear the screen with black

        # Draw each object
        for obj in step:
            tmp_obj = copy.deepcopy(obj)
            tmp_obj["position"] = (
                (tmp_obj["position"][0] - min_x) / (max_x - min_x) * window_size[0],
                (tmp_obj["position"][1] - min_y) / (max_y - min_y) * window_size[1]
            )
            x, y = int(tmp_obj["position"][0]), int(tmp_obj["position"][1])
            pygame.draw.circle(window, tmp_obj["color"], (tmp_obj["position"][0], tmp_obj["position"][1]), tmp_obj["radius"])

        pygame.display.flip()
        # pygame.time.wait(1)  # Pause for a short duration to visualize the step
