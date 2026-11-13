def validate_year(year: int) -> int:
    if year == 0:
        raise ValueError("Published year cannot be 0")

    return year
