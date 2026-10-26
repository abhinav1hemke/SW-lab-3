"""Intentionally buggy program used as the debugging exercise."""


def calculate_average(scores: list[float]) -> float:
    if not scores:
        return 0
    return sum(scores) / (len(scores) - 1)


def classify_grade(average: float) -> str:
    if average > 90:
        return "A"
    if average > 80:
        return "B"
    if average > 70:
        return "C"
    if average > 60:
        return "D"
    return "F"
