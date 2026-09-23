import numpy as np


def export_metrics_to_tsv(
    stats: dict, ranges: dict, filename: str = "results.tsv"
) -> None:

    rows = [
        ["min_night_temperature", f"{stats['min_night_temp']:.2f}"],
        ["max_day_temperature", f"{stats['max_day_temp']:.2f}"],
        ["mean_day_temperature", f"{stats['mean_day_temp']:.2f}"],
        ["mean_night_temperature", f"{stats['mean_night_temp']:.2f}"],
        ["sum_day_temperature", f"{stats['sum_day_temp']:.2f}"],
        ["sum_night_temperature", f"{stats['sum_night_temp']:.2f}"],
        ["days_count", str(stats["days_count"])],
        ["below_zero_nights", str(ranges["below_zero_nights"])],
        ["at_or_above_30_days", str(ranges["day_30_plus"])],
    ]

    tsv_data = np.array(rows, dtype=object)

    np.savetxt(
        filename,
        tsv_data,
        fmt="%s",
        delimiter="\t",
        header="metric\tvalue",
        comments="",
    )

    