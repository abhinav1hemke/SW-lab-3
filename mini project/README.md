# Mini Project: Simple Expense Tracker

## Aim

Design and develop a small Python application with an AI coding assistant
through the software development life cycle, and document the workflow from
requirements to tests.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI assistant
- Python standard library (`argparse`, `dataclasses`, `decimal`, `json`,
  `unittest`)

No third-party packages are required.

## Development Stage 1 – Requirements: `requirements.md`

The requirements define the expense tracker features, input rules, and scope.
Display them for a screenshot:

```powershell
Get-Content ".\mini project\requirements.md"
```

AI-assisted workflow: ask the coding assistant to turn the project idea into
small, testable functional and non-functional requirements. Review the draft
for clear input, output, validation, and out-of-scope items.

## Stage 2 – Design: `design.md` (excerpt)

The design separates the program into a data model, JSON storage, and CLI.
Display the design:

```powershell
Get-Content ".\mini project\design.md"
```

AI-assisted workflow: ask the assistant to propose a simple module structure
and JSON data format that satisfy `requirements.md`. Check that each requirement
maps to a module or a test.

## Stage 3 – Implementation

### `models.py` (excerpt)

`Expense` validates required fields, positive money amounts, and ISO dates.

```powershell
Get-Content ".\mini project\models.py"
```

### `storage.py`

The storage module saves and loads expenses in JSON and assigns each new
expense an ID.

```powershell
Get-Content ".\mini project\storage.py"
```

### `cli.py` (main)

The CLI provides `add`, `list`, and `summary` commands. By default, data is
stored in the user's `.expense_tracker` directory. Use `--data-file` to select
a different file.

```powershell
Get-Content ".\mini project\cli.py"
```

AI-assisted workflow: implement one module at a time, ask the assistant to
explain its changes, and compare each result with the requirements and design.
The code uses decimal arithmetic for money and reports invalid input explicitly.

## Try the application

Run these examples from the repository root. They use a separate demo file:

```powershell
python ".\mini project\cli.py" --data-file ".\mini project\demo_expenses.json" add --description "Lunch" --amount 12.50 --category Food
python ".\mini project\cli.py" --data-file ".\mini project\demo_expenses.json" list
python ".\mini project\cli.py" --data-file ".\mini project\demo_expenses.json" summary
```

The demo file is created the first time you add an expense.

## Stage 4 – Testing: `test_expenses.py` (excerpt)

Tests cover model validation, file persistence, CLI commands, totals, and
invalid input. Temporary files keep tests isolated from personal data.

```powershell
Get-Content ".\mini project\test_expenses.py"
```

### Test run

Run the test suite from the repository root:

```powershell
python -m unittest discover -s ".\mini project" -p "test_*.py" -v
```

Expected result: **11 tests passed** and `OK`. Take a screenshot of the verbose
terminal output.

AI-assisted workflow: ask the assistant to propose tests for both normal and
invalid cases, then review whether the tests correspond to requirements.
Finally, run the suite and use failures to correct the implementation.

## Conclusion

The project demonstrates an end-to-end workflow: clarify requirements, design
small modules, implement a local expense tracker, and validate behavior with
repeatable tests. AI suggestions are reviewed against requirements and verified
by running the tests.
