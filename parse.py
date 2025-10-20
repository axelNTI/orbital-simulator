import json

type planet = dict[str, str | list[float]]
DATA_DIR = "."

def parse_file(filename: str) -> list[planet] | bool:
    global DATA_DIR
    try:
        file = open(f"{DATA_DIR}/{filename}")
        data = json.load(file)
        return data
    except OSError:
        return False
