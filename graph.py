import matplotlib.pyplot as plt
import pandas as pd

def init(objects):
    global ax, lines, velocity_data
    fig, ax = plt.subplots()
    velocity_data = {i: [] for i in range(len(objects))}  # Store velocity history per object
    lines = []

    # Create a line for each object
    colors = plt.cm.get_cmap('tab10', len(objects))
    for index, obj in enumerate(objects):
        line, = ax.plot([], [], color=tuple(c/255 for c in obj["color"]), label=obj["name"])
        lines.append(line)

    ax.set_xlabel("Iteration")
    ax.set_ylabel("Velocity (m/s)")
    ax.set_title("Velocity per Object Over Time")
    ax.legend()

def graph_step(iteration, objects, interval):
    for i, obj in enumerate(objects):
        vx, vy = obj["velocity"]
        vel_mag = (vx**2 + vy**2)**0.5
        velocity_data[i].append(vel_mag)

        x_vals = range(len(velocity_data[i]))
        lines[i].set_xdata(x_vals)
        lines[i].set_ydata(velocity_data[i])

    ax.relim()
    ax.autoscale_view()

    ticks = ax.get_xticks()
    ax.set_xticklabels([int(t * interval) for t in ticks])

    plt.draw()
    plt.pause(0.001)