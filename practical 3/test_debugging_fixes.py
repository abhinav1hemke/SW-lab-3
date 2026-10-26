import unittest

from fixed import calculate_average
from fixed2 import classify_grade


class AverageFixTests(unittest.TestCase):
    def test_average_uses_the_number_of_scores(self) -> None:
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_single_score_does_not_divide_by_zero(self) -> None:
        self.assertEqual(calculate_average([75]), 75)

    def test_empty_score_list_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one score"):
            calculate_average([])

    def test_out_of_range_scores_are_rejected(self) -> None:
        for scores in ([-1], [101]):
            with self.subTest(scores=scores):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    calculate_average(scores)


class GradeBoundaryFixTests(unittest.TestCase):
    def test_boundaries_are_inclusive(self) -> None:
        expected_grades = {
            90: "A",
            80: "B",
            70: "C",
            60: "D",
            59: "F",
        }
        for score, expected in expected_grades.items():
            with self.subTest(score=score):
                self.assertEqual(classify_grade(score), expected)

    def test_scores_outside_range_are_rejected(self) -> None:
        for score in (-1, 101):
            with self.subTest(score=score):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    classify_grade(score)


if __name__ == "__main__":
    unittest.main()
