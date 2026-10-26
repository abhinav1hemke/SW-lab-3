"""Bug 2: intentionally incorrect grade-boundary comparisons."""


def classify_grade(score: float) -> str:
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    if score > 60:
        return "D"
    return "F"


if __name__ == "__main__":
    sample_score = 90
    print(f"Score: {sample_score}")
    print(f"Grade: {classify_grade(sample_score)}")
