# Practical 5: AI-Generated Unit Test Cases

## Aim

Generate unit test cases for a function/module with an AI coding assistant
and execute them using a testing framework.

## Tools

- Python 3
- AI assistant using Copilot in VS Code
- Python standard library `unittest`

## Problem statement

Test a small validation module that checks basic email formatting and password
requirements. An email must have one `@`, a nonempty local part, and a dotted
domain. A password must have at least eight characters and contain an
uppercase letter, a lowercase letter, and a digit.

## `validators.py`

The module defines `is_valid_email` and `is_valid_password`. The email
validator is intentionally a basic educational check, not a complete
implementation of the email address standard.

## AI-generated tests plus my manual test (`test_validators.py`)

The test module contains AI-assisted cases for valid inputs, invalid inputs,
password requirements, and common boundary conditions. The
`ManualValidatorTests` class adds four manually selected edge and boundary
tests. All cases use Python's `unittest` framework.

## Test execution report

From the repository root in the VS Code PowerShell terminal, run:

```powershell
python -m unittest discover -s ".\practical 5" -p "test_*.py" -v
```

The expected result is **16 tests passed**, with zero failures and errors.
See [`TEST_EXECUTION_REPORT.md`](./TEST_EXECUTION_REPORT.md) for the coverage
summary. Run this command in your own terminal and screenshot the verbose
output as the execution evidence for your manual.

## Conclusion

The AI-assisted and manually chosen tests verify typical valid and invalid
inputs along with important boundary cases. The test framework provides a
repeatable execution report to confirm the validator behavior.
