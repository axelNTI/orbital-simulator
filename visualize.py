import pygame_gui
import pygame

def visualize_simulation(simulation):
    pygame.init()

    # Set up the window
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Orbital Simulation Visualization")

    # Set up the GUI manager
    manager = pygame_gui.UIManager(window_size)

    clock = pygame.time.Clock()
    is_running = True

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
            manager.process_events(event)

        manager.update(clock.tick(60) / 1000.0)

        window.fill((0, 0, 0))  # Clear the screen with black

        # Draw each object
        for obj in step:
            obj["position"] = (
                (obj["position"][0] - min_x) / (max_x - min_x) * window_size[0],
                (obj["position"][1] - min_y) / (max_y - min_y) * window_size[1]
            )
            x, y = int(obj["position"][0]), int(obj["position"][1])
            pygame.draw.circle(window, obj["color"], (obj["position"][0], obj["position"][1]), obj["radius"])

        manager.draw_ui(window)
        pygame.display.flip()
        # pygame.time.wait(1)  # Pause for a short duration to visualize the step