import json

type planet = dict[str, str | list[float]]
data_dir = "."

def parse_file(filename: str) -> list[planet] | bool:
    global data_dir
    try:
        file = open(f"{data_dir}/{filename}")
        data = json.load(file)
        return data
    except OSError:
        return False
