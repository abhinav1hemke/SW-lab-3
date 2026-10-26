import unittest

from validators import is_valid_email, is_valid_password


class AIGeneratedEmailTests(unittest.TestCase):
    """AI-assisted test scenarios for common email validation cases."""

    def test_accepts_standard_email(self) -> None:
        self.assertTrue(is_valid_email("student@example.com"))

    def test_accepts_plus_addressing(self) -> None:
        self.assertTrue(is_valid_email("student+lab@example.co.in"))

    def test_rejects_email_without_at_sign(self) -> None:
        self.assertFalse(is_valid_email("student.example.com"))

    def test_rejects_email_with_multiple_at_signs(self) -> None:
        self.assertFalse(is_valid_email("student@@example.com"))

    def test_rejects_domain_without_dot(self) -> None:
        self.assertFalse(is_valid_email("student@example"))

    def test_rejects_email_containing_whitespace(self) -> None:
        self.assertFalse(is_valid_email("student name@example.com"))


class AIGeneratedPasswordTests(unittest.TestCase):
    """AI-assisted test scenarios for password rules and boundaries."""

    def test_accepts_password_meeting_all_rules(self) -> None:
        self.assertTrue(is_valid_password("Student123"))

    def test_rejects_password_shorter_than_eight_characters(self) -> None:
        self.assertFalse(is_valid_password("Abc1234"))

    def test_rejects_password_without_uppercase_letter(self) -> None:
        self.assertFalse(is_valid_password("student123"))

    def test_rejects_password_without_lowercase_letter(self) -> None:
        self.assertFalse(is_valid_password("STUDENT123"))

    def test_rejects_password_without_digit(self) -> None:
        self.assertFalse(is_valid_password("StudentLab"))

    def test_rejects_empty_password(self) -> None:
        self.assertFalse(is_valid_password(""))


class ManualValidatorTests(unittest.TestCase):
    """Additional manually selected edge and boundary tests."""

    def test_accepts_minimal_dotted_email_domain(self) -> None:
        self.assertTrue(is_valid_email("a@b.c"))

    def test_rejects_empty_email(self) -> None:
        self.assertFalse(is_valid_email(""))

    def test_rejects_domain_label_starting_with_hyphen(self) -> None:
        self.assertFalse(is_valid_email("student@-example.com"))

    def test_accepts_password_at_minimum_length(self) -> None:
        self.assertTrue(is_valid_password("Abcdefg1"))


if __name__ == "__main__":
    unittest.main()
