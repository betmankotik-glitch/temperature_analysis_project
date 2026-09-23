from temp_analytics.reader import load_data
from temp_analytics.stats import get_general_stats
from temp_analytics.extremes import get_extremes
from temp_analytics.ranges import get_ranges_analysis
from temp_analytics.filters import get_extreme_days
from temp_analytics.exporter import export_metrics_to_tsv


def main():
    # 1. Зчитування
    headers, dates, day_temps, night_temps = load_data("temperatures.csv")
    print(f"Заголовки у CSV: {headers}")

    # 2. Статистика
    stats = get_general_stats(day_temps, night_temps)
    print("\n--- Загальна статистика ---")
    for k, v in stats.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

    # 3. Екстремуми
    extremes = get_extremes(dates, day_temps, night_temps)
    print("\n--- Найхолодніший та найтепліший день ---")
    print(f"Індекс найхолоднішої ночі: {extremes['min_night_idx']}")
    print(f"Найнижча нічна температура: {extremes['min_night_temp']}°C (Дата: {extremes['min_night_date']})")
    print(f"Індекс найтеплішого дня: {extremes['max_day_idx']}")
    print(f"Найвища денна температура: {extremes['max_day_date']} — {extremes['max_day_temp']}°C")

    # 4. Діапазони
    ranges = get_ranges_analysis(day_temps, night_temps)
    print("\n--- Аналіз за діапазонами ---")
    for k, v in ranges.items():
        print(f"{k}: {v}")

    # 5. Фільтрація екстремальних днів
    filtered = get_extreme_days(dates, day_temps, night_temps)
    print("\n--- Днів із денною температурою >= 30°C ---:", len(filtered["days_day_gte_30"]))
    print("--- Днів із нічною температурою < -3°C ---:", len(filtered["days_night_lt_minus3"]))

    # 6. Експорт у TSV
    export_metrics_to_tsv(stats, ranges, "temperature_summary.tsv")
    print("\nРезультати збережено у файл temperature_summary.tsv!")


if __name__ == "__main__":
    main()



