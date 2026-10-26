# Design: Simple Expense Tracker

## Architecture

The application is a small local command-line program with three layers:

1. **Model (`models.py`)** defines a validated `Expense` record. It owns the
   rules for positive amounts, required text fields, and ISO-format dates.
2. **Storage (`storage.py`)** reads and writes a JSON file and assigns the
   next integer ID. It uses `Decimal` values for money and does not contain
   terminal-input or output logic.
3. **CLI (`cli.py`)** parses `add`, `list`, and `summary` commands, calls the
   model/storage functions, and prints results for the user.

## Data flow

For `add`, the CLI parses the supplied values, creates a validated `Expense`,
loads existing records, assigns an ID, and saves the complete JSON collection.
For `list` and `summary`, the CLI loads the same collection and formats the
results. The optional `--data-file` argument selects the JSON file; by default
it is stored in the user's `.expense_tracker` directory.

## Data format

```json
{
  "expenses": [
    {
      "id": 1,
      "description": "Lunch",
      "amount": "12.50",
      "category": "Food",
      "date": "2026-10-27"
    }
  ]
}
```

Amounts are stored as decimal strings to avoid binary floating-point
rounding. Dates use ISO `YYYY-MM-DD` format.

## Testing approach

Unit tests validate model rules, JSON persistence and IDs, CLI output, category
totals, and invalid-input handling. Temporary files isolate each storage test
from the user's real expense data.
