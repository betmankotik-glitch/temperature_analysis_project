import numpy as np


def get_extremes(dates: np.ndarray, day_temps: np.ndarray, night_temps: np.ndarray) -> dict:
    min_night_idx = int(np.argmin(night_temps))
    max_day_idx = int(np.argmax(day_temps))

    return {
        "min_night_idx": min_night_idx,
        "max_day_idx": max_day_idx,
        "min_night_temp": night_temps[min_night_idx],
        "min_night_date": dates[min_night_idx],
        "max_day_temp": day_temps[max_day_idx],
        "max_day_date": dates[max_day_idx],
    }

