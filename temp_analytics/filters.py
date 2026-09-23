import numpy as np


def get_extreme_days(dates: np.ndarray, day_temps: np.ndarray, night_temps: np.ndarray) -> dict:
    return {
        "days_day_gte_30": dates[day_temps >= 30],
        "days_night_lt_minus3": dates[night_temps < -3],
        "days_day_gte_25": dates[day_temps >= 25],
        "days_night_minus1_to_1": dates[(night_temps >= -1) & (night_temps <= 1)],
    }

