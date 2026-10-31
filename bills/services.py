from math import isfinite


def summarize_usage(readings: list[float]) -> dict[str, int | float]:
    """Return count, total and average for finite, nonnegative usage readings."""
    if not readings:
        raise ValueError("The reading list is empty.")
    if any(value < 0 or not isfinite(value) for value in readings):
        raise ValueError("Readings must be finite and nonnegative.")

    total = sum(readings)
    if not isfinite(total):
        raise ValueError("The total usage must be finite.")
    count = len(readings)
    return {"count": count, "total": total, "average": total / count}
