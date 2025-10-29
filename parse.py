import json

DATA_DIR = "."
DEFAULT_WINDOW_SIZE = (800, 600)

def parse_file(filename: str) -> dict[str, int | float | list[float]] | list[dict[str, str | float | int | list[int]]] | bool:
    global DATA_DIR, data
    try:
        file = open(f"{DATA_DIR}/{filename}")
        data = json.load(file)
        return data
    except OSError:
        return False

def objects() -> list[dict[str, str | float | int | list[int]]] | bool:
    if "objects" not in data:
        return False
    for o in data["objects"]:
        if "relative_position" in o and o["relative_position"] != "":
            relative_to = o["relative_position"]
            for other in data["objects"]:
                if other["name"] == relative_to:
                    o["position"][0] += other["position"][0]
                    o["position"][1] += other["position"][1]
    return data["objects"]

def _get_integer_by_key(key: str, default: int | bool = False) -> int | bool:
    if not key in data: return default
    try:
        result = int(data[key])
        return result
    except ValueError:
        return False

def iterations() -> int | bool:
    return _get_integer_by_key("iterations")

def time_resolution() -> int | bool:
    return _get_integer_by_key("time_resolution", default = 1)

def window_size() -> tuple[int, int] | bool:
    if "window_size" not in data: 
        return DEFAULT_WINDOW_SIZE
    try:
        x = int(data["window_size"][0])
        y = int(data["window_size"][1])
        return (x, y)
    except ValueError:
        return False

def vis_interval() -> int | bool:
    return _get_integer_by_key("visualization_interval", default = 1)

def _get_initial_scale(axis: str) -> tuple[int, int] | bool:
    initial_min = _get_integer_by_key(f"min_{axis}", -1)
    initial_max = _get_integer_by_key(f"max_{axis}", 1)
    if not (initial_min or initial_max):
        return False
    min_val = min(initial_min, -1) # Make sure minimum value can't be 0 for divisions
    max_val = max(initial_max, 1) # Make sure max value can't be the same as minimum value, also to avoid division by 0
    return (min_val, max_val)

def initial_scale_x() -> tuple[int, int] | bool:
    return _get_initial_scale("x")

def initial_scale_y() -> tuple[int, int] | bool:
    return _get_initial_scale("y")
