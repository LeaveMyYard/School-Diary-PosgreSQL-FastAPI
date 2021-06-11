from datetime import datetime, timedelta


def calc_grade(year_started: int) -> int:
    return (datetime.now() - timedelta(days=180)).year - year_started + 1
