# Practical 6: AI-Based Static Code Analysis and Vulnerability Scanning

## Aim

Use static analysis tools with an AI coding assistant to identify code smells,
bugs, and security issues in a sample project, then verify the fixes.

## Tools

- Python 3
- AI assistant using Copilot in VS Code
- Ruff for Python linting and code-smell checks
- Bandit for Python security scanning
- Python `unittest` for fix verification

## Sample project findings

The intentionally flawed program is
`sample_project\before\app.py`. It contains an unused import, a hard-coded
demonstration token, unsafe use of `eval`, and an incorrect percentage
discount formula. The embedded token is fake and must not be used as a real
credential.

The fixed example is `sample_project\after\app.py`. It removes the unused
import, parses only Python literals, reads the token from an environment
variable, validates inputs, and calculates percentage discounts correctly.
Never put real secrets in source code; use an approved secret manager for
production applications.

## Install the static analysis tools

From the repository root in the VS Code PowerShell terminal:

```powershell
python -m pip install -r ".\practical 6\requirements.txt"
```

## Static analysis output

Run Ruff on the flawed example. It should report the unused import:

```powershell
python -m ruff check ".\practical 6\sample_project\before"
```

Run Bandit on the flawed example. `--exit-zero` lets the terminal proceed
normally while the scanner displays its findings:

```powershell
python -m bandit -r ".\practical 6\sample_project\before" -f txt --exit-zero
```

The scan should report the unsafe `eval` and hard-coded demonstration token.
These are deliberate educational findings, not real credentials.
In this sample run, Bandit reports two findings: B105 (hard-coded
demonstration token) and B307 (use of `eval`). Ruff reports one F401 finding
for the unused `json` import.

Running the two sample programs also demonstrates the calculation bug:

```powershell
python ".\practical 6\sample_project\before\app.py"
python ".\practical 6\sample_project\after\app.py"
```

The first prints `Discounted price: 0.00`; the fixed version prints
`Discounted price: 90.00`.

## Verify the fixes

Ruff should report that the fixed example is clean:

```powershell
python -m ruff check ".\practical 6\sample_project\after"
```

Bandit should report `No issues identified` in the fixed example:

```powershell
python -m bandit -r ".\practical 6\sample_project\after" -f txt
```

Run the unit tests:

```powershell
python -m unittest discover -s ".\practical 6" -p "test_*.py" -v
```

The tests verify safe record parsing, missing-token handling, discount
calculations, and invalid input handling. The expected result is 8 passing
tests.

## Screenshot instructions

Take separate VS Code terminal screenshots showing the command and output for:

1. Ruff findings in the `before` example.
2. Bandit findings in the `before` example.
3. Clean Ruff output for the `after` example.
4. Bandit's no-issues report for the `after` example.
5. The test execution report showing 8 tests and `OK`.

## Conclusion

Static analysis identified a maintainability issue and two security hazards,
while a functional test exposed an incorrect discount calculation. The
refactored example addresses those issues, and clean scanner results plus
passing tests provide evidence that the changes were verified.
