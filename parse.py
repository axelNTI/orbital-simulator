import json

DATA_DIR = "."
DEFAULT_WINDOW_SIZE = (800, 600)

def parse_file(filename: str) -> list[dict[str, str | list[float]]] | bool:
    global DATA_DIR, data
    try:
        file = open(f"{DATA_DIR}/{filename}")
        data = json.load(file)
        return data
    except OSError:
        return False

def objects():
    return data["objects"]

def iterations():
    return data["iterations"]

def time_resolution():
    if not data["time_resolution"]: return 1
    return data["time_resolution"]

def window_size():
    if not data["window_size"]: return DEFAULT_WINDOW_SIZE
    return data["window_size"]

def vis_interval():
    if not data["visualization_interval"]: return 1
    return data["visualization_interval"]

def initial_scale_x():
    min_x = min(data["min_x"], -1)
    max_x = max(data["max_x"], 1)
    return (min_x, max_x)

def initial_scale_y():
    min_y = min(data["min_y"], -1)
    max_y = max(data["max_y"], 1)
    return (min_y, max_y)
