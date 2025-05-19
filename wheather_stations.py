# Coding Challenge #3
# bool is only True or False
def calc_rainfall_stats(daily_readings: list[float]) -> dict[str, float | int | bool]:
    if not daily_readings:
        return {
            'total_rainfall': 0.0,
            'average_rainfall': 0.0,
            'rainy_days': 0,
            'dry_spell_warning': False,

        }

    total_rainfall = float(round(sum(daily_readings), 2))

    average_rainfall = float(round(total_rainfall / len(daily_readings), 2))

    rainy_days = sum(1 for rainfall in daily_readings if rainfall > 0)

    # dry_spell_warning
    current_dry_count = 0
    max_dry_count = 0
    for rainfall in daily_readings:
        if rainfall == 0.0:
            current_dry_count += 1
        else:
            max_dry_count = max(max_dry_count, current_dry_count)
            current_dry_count = 0
    max_dry_count = max(max_dry_count, current_dry_count)
    dry_spell_warning = max_dry_count > 5

    return {
        'total_rainfall': total_rainfall,
        'average_rainfall': average_rainfall,
        'rainy_days': rainy_days,
        'dry_spell_warning': dry_spell_warning
    }
