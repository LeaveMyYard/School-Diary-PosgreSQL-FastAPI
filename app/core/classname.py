GRADES_TOTAL = 11


def format_display_name(grade: int, name: str, year_started: int) -> str:
    if grade <= GRADES_TOTAL:
        return f"{grade}-{name}"
    return f"{name}, graduated at {year_started + GRADES_TOTAL}"
