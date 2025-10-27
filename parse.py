import json

DATA_DIR = "."

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
    return data["time_resolution"]

def window_size():
    return data["window_size"]

def vis_interval():
    return data["visualization_interval"]

def initial_scale_x():
    min_x = data["min_x"]
    max_x = data["max_x"]
    return (min_x, max_x)

def initial_scale_y():
    min_y = data["min_y"]
    max_y = data["max_y"]
    return (min_y, max_y)
