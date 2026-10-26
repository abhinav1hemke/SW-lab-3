# Practical 4: AI-Assisted Code Refactoring and Auto-Documentation

## Aim

Refactor legacy/unstructured code with an AI coding assistant and add
documentation to the refactored program.

## Tools

- Python 3
- AI assistant using Copilot in VS Code
- Python standard library: `dataclasses`, `unittest`

## Problem statement

The program prints an invoice for products. Each product has a name, unit
price, and quantity. It applies a 10% discount when the subtotal is at least
INR 500, then calculates 8% tax on the discounted subtotal.

## Step 1/2 – `messy.py` (original)

The original program uses short variable names, performs all calculations in
one top-level block, and mixes invoice calculation with printing.

### Terminal

Open the repository in VS Code, choose **Terminal → New Terminal**, then run
this command from the repository root:

```powershell
python ".\practical 4\messy.py"
```

Expected output:

```text
INVOICE
Notebook x 2: INR 240.00
Pen pack x 1: INR 80.00
Backpack x 1: INR 300.00
Subtotal: INR 620.00
Discount: INR 62.00
Tax: INR 44.64
Total: INR 602.64
```

Take a screenshot showing the terminal command and its output for Steps 1/2.

## AI explanation of the refactoring

The original code is difficult to maintain because calculations and display
logic are combined, variable names do not explain their purpose, and discount
and tax values are embedded directly in the calculation block. The refactor
uses descriptive names and constants, puts invoice calculation in a reusable
function, groups results in an immutable `Invoice` data class, and separates
printing from calculation. Docstrings explain the purpose and behavior of the
module, data class, and functions.

## Step 3–5 – AI-refactored code saved as `clean.py`

Run the refactored program from the repository root:

```powershell
python ".\practical 4\clean.py"
```

It should print the same invoice output as `messy.py`. Take a screenshot
showing the command and output for Steps 3–5.

## Verify the refactor

Run the automated tests:

```powershell
python -m unittest discover -s ".\practical 4" -p "test_*.py" -v
```

The tests cover regular invoice calculations, no-discount calculations,
discount eligibility at the threshold, and an empty product list. The
expected result is 4 passing tests.

## Result and conclusion

The refactored program keeps the original sample invoice output while
organizing calculations and presentation into documented, reusable code.
Automated tests verify the calculation behavior, including discount and tax
rules.
