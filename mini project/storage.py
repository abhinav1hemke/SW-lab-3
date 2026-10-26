"""JSON-file persistence for expense records."""

import json
from pathlib import Path

from models import Expense


def load_expenses(path: Path) -> list[Expense]:
    """Load saved expenses, returning an empty list when the file is absent."""
    if not path.exists():
        return []

    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"expense file contains invalid JSON: {path}") from error

    if not isinstance(content, dict) or not isinstance(
        content.get("expenses"), list
    ):
        raise TypeError("expense file must contain an 'expenses' list")

    expenses = []
    for index, record in enumerate(content["expenses"]):
        if not isinstance(record, dict):
            raise TypeError(f"expense record {index + 1} must be an object")
        expenses.append(Expense.from_dict(record))
    return expenses


def save_expenses(path: Path, expenses: list[Expense]) -> None:
    """Save all expenses as readable JSON, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = {"expenses": [expense.to_dict() for expense in expenses]}
    path.write_text(
        json.dumps(content, indent=2) + "\n",
        encoding="utf-8",
    )


def add_expense(path: Path, expense: Expense) -> Expense:
    """Assign the next ID, persist the expense, and return the saved record."""
    expenses = load_expenses(path)
    next_id = max((item.id for item in expenses), default=0) + 1
    saved_expense = Expense(
        id=next_id,
        description=expense.description,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
    )
    expenses.append(saved_expense)
    save_expenses(path, expenses)
    return saved_expense
