import numpy as np


def get_general_stats(day_temps: np.ndarray, night_temps: np.ndarray) -> dict:
    return {
        "days_count": len(day_temps),
        "max_day_temp": np.max(day_temps),
        "min_night_temp": np.min(night_temps),
        "mean_day_temp": np.mean(day_temps),
        "mean_night_temp": np.mean(night_temps),
        "median_day_temp": np.median(day_temps),
        "median_night_temp": np.median(night_temps),
        "sum_day_temp": np.sum(day_temps),
        "sum_night_temp": np.sum(night_temps),
    }

