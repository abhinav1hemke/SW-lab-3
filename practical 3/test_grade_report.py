import unittest

from grade_report import calculate_average, classify_grade


class CalculateAverageTests(unittest.TestCase):
    def test_calculates_average_using_number_of_scores(self) -> None:
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_single_score_is_its_own_average(self) -> None:
        self.assertEqual(calculate_average([75]), 75)

    def test_empty_scores_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one score"):
            calculate_average([])

    def test_scores_outside_valid_range_are_rejected(self) -> None:
        for scores in ([-1, 50], [50, 101]):
            with self.subTest(scores=scores):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    calculate_average(scores)


class ClassifyGradeTests(unittest.TestCase):
    def test_grade_thresholds_are_inclusive(self) -> None:
        cases = {
            90: "A",
            80: "B",
            70: "C",
            60: "D",
            59.99: "F",
        }
        for score, expected in cases.items():
            with self.subTest(score=score):
                self.assertEqual(classify_grade(score), expected)

    def test_averages_outside_valid_range_are_rejected(self) -> None:
        for average in (-1, 101):
            with self.subTest(average=average):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    classify_grade(average)


if __name__ == "__main__":
    unittest.main()
