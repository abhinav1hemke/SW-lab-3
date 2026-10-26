import unittest

from sample_project.after.app import (
    ENVIRONMENT_SETTING_NAME,
    calculate_discount,
    get_api_token,
    parse_user_record,
)


class ParseUserRecordTests(unittest.TestCase):
    def test_parses_dictionary_literal(self) -> None:
        self.assertEqual(parse_user_record("{'name': 'Ada', 'active': True}"),
                         {"name": "Ada", "active": True})

    def test_rejects_non_dictionary_literal(self) -> None:
        with self.assertRaisesRegex(TypeError, "must contain a dictionary"):
            parse_user_record("[1, 2, 3]")

    def test_rejects_invalid_literal(self) -> None:
        with self.assertRaisesRegex(ValueError, "valid dictionary literal"):
            parse_user_record("not valid Python")


class GetApiTokenTests(unittest.TestCase):
    def test_reads_token_from_environment_mapping(self) -> None:
        self.assertEqual(
            get_api_token({ENVIRONMENT_SETTING_NAME: "test-token"}),
            "test-token",
        )

    def test_missing_token_is_reported(self) -> None:
        with self.assertRaisesRegex(ValueError, "Set the PRACTICAL6_API_TOKEN"):
            get_api_token({})


class CalculateDiscountTests(unittest.TestCase):
    def test_calculates_percentage_discount_correctly(self) -> None:
        self.assertEqual(calculate_discount(100, 10), 90)

    def test_zero_and_full_discounts(self) -> None:
        self.assertEqual(calculate_discount(100, 0), 100)
        self.assertEqual(calculate_discount(100, 100), 0)

    def test_rejects_invalid_price_and_discount(self) -> None:
        for price, discount in ((-1, 10), (100, -1), (100, 101)):
            with self.subTest(price=price, discount=discount):
                with self.assertRaises(ValueError):
                    calculate_discount(price, discount)


if __name__ == "__main__":
    unittest.main()
