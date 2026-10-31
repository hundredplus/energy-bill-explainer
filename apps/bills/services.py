def summarize_usage(readings: list[float]) -> dict[str, int | float]:
    """Return count, total, and average of a list of numbers.
    Raise a ValueError if the list is empty."""
    
    if not readings:
        raise ValueError("The reading list is empty.")
    
    total = sum(readings)
    count = len(readings)
    average = total / count
    
    return {
        "count": count,
        "total": total,
        "average": average
    }
    