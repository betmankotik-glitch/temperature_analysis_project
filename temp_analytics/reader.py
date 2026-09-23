import numpy as np


def load_data(file_path: str = "temperatures.csv"):

    with open(file_path, "r", encoding="utf-8") as f:
        headers = np.array(f.readline().strip().split(","))


    data = np.genfromtxt(
        file_path,
        delimiter=",",
        skip_header=1,
        dtype=None,
        encoding="utf-8",
    )


    dates = np.array([row[0] for row in data])
    day_temps = np.array([row[1] for row in data], dtype=float)
    night_temps = np.array([row[2] for row in data], dtype=float)

    return headers, dates, day_temps, night_temps