"""Calculate a student's average score and corresponding letter grade."""

from collections.abc import Sequence


def calculate_average(scores: Sequence[float]) -> float:
    """Return the arithmetic mean of scores in the range 0 through 100."""
    if not scores:
        raise ValueError("at least one score is required")
    if any(not 0 <= score <= 100 for score in scores):
        raise ValueError("scores must be between 0 and 100")
    return sum(scores) / len(scores)


def classify_grade(average: float) -> str:
    """Map an average score to a letter grade."""
    if not 0 <= average <= 100:
        raise ValueError("average must be between 0 and 100")
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main() -> None:
    raw_scores = input("Enter scores separated by spaces: ")
    try:
        scores = [float(value) for value in raw_scores.split()]
        average = calculate_average(scores)
        grade = classify_grade(average)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
