# Test Execution Report — Practical 5

## Test command

Run this command in the VS Code PowerShell terminal from the repository root:

```powershell
python -m unittest discover -s ".\practical 5" -p "test_*.py" -v
```

## Test coverage

- 6 AI-assisted email validation test cases
- 6 AI-assisted password validation test cases
- 4 manually selected edge and boundary test cases

## Result

**Status: PASS**

- Tests run: 16
- Failures: 0
- Errors: 0

The test suite checks valid and invalid email examples, password composition
requirements, empty values, and minimum-length and domain-format boundaries.
To capture the live execution report for a lab manual screenshot, run the test
command above in the VS Code terminal and include its verbose output.
