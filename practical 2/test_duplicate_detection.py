import unittest

from duplicate_detection import (
    build_dataset,
    find_duplicates_naive,
    find_duplicates_optimized,
)


class DuplicateDetectionTests(unittest.TestCase):
    def test_empty_input(self) -> None:
        self.assertEqual(find_duplicates_naive([]), [])
        self.assertEqual(find_duplicates_optimized([]), [])

    def test_input_without_duplicates(self) -> None:
        values = [1, 2, 3, 4]
        self.assertEqual(find_duplicates_naive(values), [])
        self.assertEqual(find_duplicates_optimized(values), [])

    def test_repeated_values_are_returned_once_in_order(self) -> None:
        values = [5, 2, 5, 3, 2, 5, 4, 3]
        expected = [5, 2, 3]
        self.assertEqual(find_duplicates_naive(values), expected)
        self.assertEqual(find_duplicates_optimized(values), expected)

    def test_implementations_match_on_benchmark_dataset(self) -> None:
        values = build_dataset(50)
        self.assertEqual(
            find_duplicates_naive(values),
            find_duplicates_optimized(values),
        )

    def test_negative_dataset_size_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            build_dataset(-1)


if __name__ == "__main__":
    unittest.main()
