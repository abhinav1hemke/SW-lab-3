# Practical 3: AI-Assisted Debugging

## Aim

Identify and fix errors in a buggy program with an AI coding assistant, then
verify the suggested fix.

## Problem statement

The program calculates the average of student scores and assigns a letter
grade. Valid scores and averages are between 0 and 100 inclusive. Grade
boundaries are A (90-100), B (80-89.99), C (70-79.99), D (60-69.99), and F
(below 60).

## Tools

- Python 3
- AI assistant using Copilot SDK in VS Code
- Python standard library `unittest`

## Debugging process and identified defects

`buggy_grade_report.py` is the original program containing the errors. Its
`calculate_average` function divides by `len(scores) - 1` instead of the
number of scores. This gives an incorrect average for lists with multiple
scores and raises a division-by-zero error for one score. It also returns 0 for
an empty list, which looks like a valid result instead of reporting invalid
input.

The grade comparisons use `>` rather than `>=`, so exact boundary scores (for
example, 90) are assigned the next lower grade.

`grade_report.py` fixes these defects by dividing by the actual number of
scores, reporting empty or out-of-range input with `ValueError`, and using
inclusive grade thresholds. Its command-line interaction also reports invalid
input clearly.

## Run the practical

From the repository root in the VS Code PowerShell terminal, run the tests:

```powershell
python -m unittest discover -s ".\practical 3" -p "test_*.py" -v
```

Run the corrected program:

```powershell
python ".\practical 3\grade_report.py"
```

Enter scores separated by spaces when prompted, for example:

```text
80 90 100
```

Expected output:

```text
Average: 90.00
Grade: A
```

Try a boundary score such as `90`, a single score, invalid input, and an empty
line to verify the fix and input handling.

## Result and conclusion

The tests verify the average calculation, single and empty inputs, score
validation, inclusive grade boundaries, and average validation. Passing these
tests confirms the corrected program behaves as specified for the tested
cases.
