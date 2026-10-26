# Practical 2: AI-Assisted Code Writing and Optimization

## Aim

Write and optimize a program with an AI coding assistant, then evaluate the
efficiency of the generated and optimized solutions.

## Problem statement

Given a sequence of integers, return every value that occurs more than once.
Each duplicate is returned once, in the order in which it first appears.

## Tools

- Python 3
- AI assistant using Copilot SDK in VS Code
- Python standard library (`argparse`, `statistics`, `time`, and `unittest`)

## Implementations

`duplicate_detection.py` contains two implementations of the same task:

1. `find_duplicates_naive` scans the remaining sequence for each value. This
   straightforward baseline takes O(n^2) time in the worst case and O(d) space
   for the output, where `d` is the number of distinct duplicates.
2. `find_duplicates_optimized` tracks values in sets while traversing the
   sequence once. It takes O(n) average time and O(n) additional space.

Both implementations preserve the same output order and are compared for
correctness before benchmarking. The benchmark reports median runtime across
multiple runs and the measured speedup for the current machine.

## Run the practical

From the repository root in PowerShell:

```powershell
python ".\practical 2\duplicate_detection.py" --size 5000 --repeats 3
```

Run the tests:

```powershell
python -m unittest discover -s ".\practical 2" -p "test_*.py" -v
```

Increase `--size` to observe how the runtime difference changes as input grows.
Benchmark timings vary by machine and system load; use the output from your own
run as the measured result rather than treating any single timing as universal.

### Sample measurement

One local run with `--size 5000 --repeats 3` processed 7,500 values and found
2,500 duplicates:

| Implementation | Median runtime |
| --- | ---: |
| Naive | 0.420589 seconds |
| Optimized | 0.000590 seconds |

Measured speedup: **712.62x** on that run. These timings are machine- and
load-dependent; rerun the benchmark to obtain your own measurements.

## Result and conclusion

The tests verify that both approaches return the same duplicates, including
empty input, inputs without duplicates, and repeated values. On larger inputs,
the set-based solution is expected to scale better because it avoids repeatedly
scanning the remaining sequence. Record the measured runtimes and speedup from
your run when submitting the lab record.
