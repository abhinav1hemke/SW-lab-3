"""Bug 1: corrected average calculation."""


def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("at least one score is required")
    if any(not 0 <= score <= 100 for score in scores):
        raise ValueError("scores must be between 0 and 100")
    return sum(scores) / len(scores)


if __name__ == "__main__":
    sample_scores = [75]
    print(f"Scores: {sample_scores}")
    print(f"Average: {calculate_average(sample_scores):.2f}")
