import numpy as np


def get_ranges_analysis(day_temps: np.ndarray, night_temps: np.ndarray) -> dict:
    return {
        "below_zero_nights": int(np.sum(night_temps < 0)),
        "day_0_to_9": int(np.sum((day_temps >= 0) & (day_temps <= 9))),
        "day_10_to_19": int(np.sum((day_temps >= 10) & (day_temps <= 19))),
        "day_20_to_29": int(np.sum((day_temps >= 20) & (day_temps <= 29))),
        "day_30_plus": int(np.sum(day_temps >= 30)),
    }

