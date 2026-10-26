"""Regression tests for payment total calculations."""

import unittest

from payments import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_adds_processing_fee_once(self) -> None:
        self.assertEqual(calculate_total(100.00, 8.00), 108.00)

    def test_zero_fee_leaves_amount_unchanged(self) -> None:
        self.assertEqual(calculate_total(100.00, 0.00), 100.00)

    def test_rounds_total_to_cents(self) -> None:
        self.assertEqual(calculate_total(10.105, 0.005), 10.11)

    def test_rejects_negative_amount_or_fee(self) -> None:
        for amount, fee in ((-1.00, 1.00), (1.00, -1.00)):
            with self.subTest(amount=amount, fee=fee), self.assertRaises(
                ValueError
            ):
                calculate_total(amount, fee)


if __name__ == "__main__":
    unittest.main()
