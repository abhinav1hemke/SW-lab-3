"""Bug 1: intentionally incorrect average calculation."""


def calculate_average(scores: list[float]) -> float:
    return sum(scores) / (len(scores) - 1)


if __name__ == "__main__":
    sample_scores = [75]
    print(f"Scores: {sample_scores}")
    print(f"Average: {calculate_average(sample_scores):.2f}")
