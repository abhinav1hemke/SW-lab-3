# Practical 3: AI-Assisted Debugging

## Aim

Identify and fix errors in buggy programs with an AI coding assistant, then
verify the fixes.

## Tools

- Python 3
- AI assistant using Copilot in VS Code
- Python `unittest`

## Bug 1 – `buggy.py` (Step 1)

### Run and traceback

From the repository root in the VS Code PowerShell terminal:

```powershell
python ".\practical 3\buggy.py"
```

Example traceback (file paths and Python's source-line markers can vary by
computer and Python version):

```text
Scores: [75]
Traceback (most recent call last):
  File "...\practical 3\buggy.py", line 11, in <module>
    print(f"Average: {calculate_average(sample_scores):.2f}")
                      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "...\practical 3\buggy.py", line 5, in calculate_average
    return sum(scores) / (len(scores) - 1)
           ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

### AI explanation of the root cause

The average function divides the sum by `len(scores) - 1`. With the one-score
sample, the denominator is zero, so Python raises `ZeroDivisionError`. For
larger lists, subtracting one also makes the calculated average incorrect. An
empty list would also make this expression invalid. The divisor should be the
number of scores, and an empty list should be rejected explicitly.

### `fixed.py` and output

Run the corrected version:

```powershell
python ".\practical 3\fixed.py"
```

Expected output:

```text
Scores: [75]
Average: 75.00
```

The corrected function divides by `len(scores)` and rejects empty lists and
scores outside the valid 0–100 range.

## Bug 2 – wrong operator (Steps 8 and 9): `buggy2.py`

Run the program with the boundary score 90:

```powershell
python ".\practical 3\buggy2.py"
```

Expected output from the buggy program:

```text
Score: 90
Grade: B
```

### AI explanation of the root cause

The grade conditions use strict `>` comparisons. Therefore, a score exactly
equal to 90 does not satisfy `score > 90`; it falls through to `score > 80`
and is incorrectly classified as B. Grade boundaries are inclusive, so the
conditions must use `>=`.

### `fixed2.py` and output

Run the corrected version:

```powershell
python ".\practical 3\fixed2.py"
```

Expected output:

```text
Score: 90
Grade: A
```

The corrected function uses inclusive boundaries and rejects scores outside
the valid 0–100 range.

## Verify the fixes

Run the automated tests:

```powershell
python -m unittest discover -s ".\practical 3" -p "test_*.py" -v
```

The tests check average calculations, the one-score and empty-list cases,
valid score ranges, and each grade boundary. The expected result is 6 passing
tests.

## VS Code terminal steps for screenshots

1. Open the `SW-lab-3` repository folder in VS Code.
2. Open **Terminal → New Terminal**. The commands below use PowerShell.
3. Change to the repository folder (adjust the path if you saved it elsewhere):

```powershell
cd "D:\MDM\Software Lab -3\SW-lab-3"
```

Run each command separately and take a screenshot showing the command and its
output. The commands are run from the repository root.

### Screenshot 1: Bug 1 traceback

```powershell
python ".\practical 3\buggy.py"
```

The program prints `Scores: [75]` followed by a `ZeroDivisionError` traceback.
The traceback is the expected result for this intentionally buggy program.

### Screenshot 2: Bug 1 fixed output

```powershell
python ".\practical 3\fixed.py"
```

Expected output:

```text
Scores: [75]
Average: 75.00
```

### Screenshot 3: Bug 2 wrong-operator output

```powershell
python ".\practical 3\buggy2.py"
```

Expected output:

```text
Score: 90
Grade: B
```

This is the incorrect result from the buggy program.

### Screenshot 4: Bug 2 fixed output

```powershell
python ".\practical 3\fixed2.py"
```

Expected output:

```text
Score: 90
Grade: A
```

### Screenshot 5: Fix verification tests

```powershell
python -m unittest discover -s ".\practical 3" -p "test_*.py" -v
```

The final lines should show `Ran 6 tests` and `OK`.

## Result and conclusion

Both bugs were reproduced with small, repeatable examples. The AI-suggested
root causes were verified by running the buggy programs, and the fixes were
checked with expected output and automated tests.
