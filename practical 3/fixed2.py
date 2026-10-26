"""Bug 2: corrected inclusive grade-boundary comparisons."""


def classify_grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    sample_score = 90
    print(f"Score: {sample_score}")
    print(f"Grade: {classify_grade(sample_score)}")
