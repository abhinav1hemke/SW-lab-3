# Practical 10: AI-Assisted Automated UI Testing

## Aim

Write and execute Selenium UI tests with an AI coding assistant, then evaluate
the accuracy of the generated test cases against the login page behavior.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI tool
- Selenium WebDriver
- Google Chrome (Selenium Manager can locate or manage the driver)

## Setup

From the repository root, install Selenium:

```powershell
python -m pip install -r ".\practical 10\requirements.txt"
```

Install Google Chrome if it is not available. Selenium Manager will locate or
download the matching ChromeDriver when the tests run.

## Step 1 – Page under test: `login.html` (script excerpt)

The page is a local demonstration login form. The valid sample credentials are
`student@example.com` and `DemoPass123!`; do not use these as real credentials.
Display the page source for a screenshot:

```powershell
Get-Content ".\practical 10\login.html"
```

## Step 2 – Selenium test suite: `test_login_ui.py` (excerpt)

The Selenium suite checks valid credentials, invalid credentials, required
email/password fields, and malformed email input. View the tests:

```powershell
Get-Content ".\practical 10\test_login_ui.py"
```

## Step 3 – Run the tests

From the repository root:

```powershell
python ".\practical 10\test_login_ui.py"
```

The test runner launches Chrome in headless mode and opens the local HTML page.
The expected result is 6 passing tests and an accuracy report of
`6/6 executed scenarios passed (100%)`.

## Step 4 – Accuracy of the test cases

Accuracy is reported as the number of executed scenarios whose observed UI
behavior matched the expected result divided by the number of executed
scenarios. The runner also reports how many of the six planned scenarios were
executed. This is a sample-level pass rate, not a guarantee of complete
real-world authentication coverage.

Take a screenshot of the terminal showing the command, all test results, and
the accuracy and scenario-coverage lines.

## Conclusion

The browser-driven checks validate expected login form behavior and report a
measurable test-case pass rate. The sample is a static client-side demonstration
only; it is not a production authentication service.
