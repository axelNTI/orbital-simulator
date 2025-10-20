import json

DATA_DIR = "."

def parse_file(filename: str) -> list[dict[str, str | list[float]]] | bool:
    global DATA_DIR
    try:
        file = open(f"{DATA_DIR}/{filename}")
        data = json.load(file)
        return data
    except OSError:
        return False
