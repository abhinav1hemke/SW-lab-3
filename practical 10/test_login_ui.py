"""Selenium UI tests and an accuracy summary for the sample login page."""

import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_PAGE = Path(__file__).with_name("login.html").as_uri()
EXPECTED_SCENARIOS = 6


class LoginUITests(unittest.TestCase):
    """Exercise the login page's success, validation, and failure behaviors."""

    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1280,900")
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.get(LOGIN_PAGE)

    def submit(self, email: str, password: str) -> None:
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-form button[type='submit']"
        ).click()

    def message(self) -> str:
        message = self.driver.find_element(By.ID, "message")
        self.wait.until(lambda _driver: message.text != "")
        return message.text

    def test_valid_credentials_show_success(self) -> None:
        self.submit("student@example.com", "DemoPass123!")
        self.assertEqual(self.message(), "Sign-in successful.")

    def test_invalid_password_shows_error(self) -> None:
        self.submit("student@example.com", "wrong-password")
        self.assertEqual(self.message(), "Invalid email or password.")

    def test_unregistered_email_shows_error(self) -> None:
        self.submit("unknown@example.com", "DemoPass123!")
        self.assertEqual(self.message(), "Invalid email or password.")

    def test_empty_email_is_blocked_by_browser_validation(self) -> None:
        self.driver.find_element(By.ID, "password").send_keys("DemoPass123!")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-form button[type='submit']"
        ).click()
        email = self.driver.find_element(By.ID, "email")
        self.assertFalse(
            self.driver.execute_script(
                "return arguments[0].validity.valid;", email
            )
        )
        self.assertEqual(self.driver.find_element(By.ID, "message").text, "")

    def test_empty_password_is_blocked_by_browser_validation(self) -> None:
        self.driver.find_element(By.ID, "email").send_keys("student@example.com")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-form button[type='submit']"
        ).click()
        password = self.driver.find_element(By.ID, "password")
        self.assertFalse(
            self.driver.execute_script(
                "return arguments[0].validity.valid;", password
            )
        )
        self.assertEqual(self.driver.find_element(By.ID, "message").text, "")

    def test_malformed_email_is_blocked_by_browser_validation(self) -> None:
        self.driver.find_element(By.ID, "email").send_keys("not-an-email")
        self.driver.find_element(By.ID, "password").send_keys("DemoPass123!")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-form button[type='submit']"
        ).click()
        email = self.driver.find_element(By.ID, "email")
        self.assertFalse(
            self.driver.execute_script(
                "return arguments[0].validity.valid;", email
            )
        )
        self.assertEqual(self.driver.find_element(By.ID, "message").text, "")


def main() -> int:
    """Run UI tests and report the proportion of cases that met expectations."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(LoginUITests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    total = result.testsRun
    passed = total - len(result.failures) - len(result.errors) - len(result.skipped)
    accuracy = round(passed / total * 100) if total else 0
    print(
        f"Test-case accuracy: {passed}/{total} executed scenarios passed "
        f"({accuracy}%)."
    )
    print(
        f"Scenario coverage: {min(total, EXPECTED_SCENARIOS)}/"
        f"{EXPECTED_SCENARIOS} expected scenarios executed."
    )
    return 0 if result.wasSuccessful() and total == EXPECTED_SCENARIOS else 1


if __name__ == "__main__":
    raise SystemExit(main())
