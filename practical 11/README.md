# Practical 11: AI-Based CI/CD Build Log Analysis

## Aim

Analyze a CI build log with an AI coding assistant, identify the probable cause
of failure, and verify the diagnosis against the corrected application code.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI tool
- GitHub Actions (workflow example)
- Python standard library (`unittest`)

## Step 1 – CI pipeline: `.github/workflows/ci.yml`

This practical includes a GitHub Actions workflow at the repository root that
tests the corrected payment calculation, exercises the log analyzer, and
verifies the historical failure diagnosis. Show the workflow:

```powershell
Get-Content ".\.github\workflows\ci.yml"
```

The committed workflow runs the corrected tests, so it should finish green.
`build.log` is a saved example of the earlier failing run, before the fix.

## Step 2 – Application code: `payments.py` (excerpt)

The corrected `calculate_total` function adds the payment amount and
processing fee exactly once:

```powershell
Get-Content ".\practical 11\payments.py"
```

## Step 3 – Build log from the failing run: `build.log`

The saved CI log shows a test expecting `108.00` for an amount of `100.00` with
an `8.00` fee, while the failing implementation returned `116.00`.

```powershell
Get-Content ".\practical 11\build.log"
```

## Step 4 – Log analyser: `analyze_log.py` (excerpt)

The analyzer identifies the failed test and source location, compares expected
and actual totals, and reports a probable cause. It saves its report as
`analysis_report.md`.

```powershell
Get-Content ".\practical 11\analyze_log.py"
```

## Step 5 – Analysis report

Run the analyzer from the repository root:

```powershell
python ".\practical 11\analyze_log.py" ".\practical 11\build.log"
```

Expected diagnosis: the fee was probably added twice. The report is also saved
as `analysis_report.md`:

```powershell
Get-Content ".\practical 11\analysis_report.md"
```

## Step 6 – Verify the probable cause

Run the verifier:

```powershell
python ".\practical 11\verify_cause.py"
```

Expected output confirms that the historical failure is consistent with
adding the fee twice and that the corrected function returns `108.00` for
`100.00 + 8.00`.

Run all practical tests:

```powershell
python -m unittest discover -s ".\practical 11" -p "test_*.py" -v
```

The expected result is 7 passing tests and `OK`. Capture terminal screenshots
for the workflow, application code, failing log, analyzer, report, and
verification output.

## Conclusion

The analyzer turns a failing test log into a specific, evidence-based
hypothesis. A reproduction against the corrected payment function and passing
regression tests verify that charging the fee twice explains the recorded
failure.
