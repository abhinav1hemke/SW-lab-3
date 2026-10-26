"""Command-line interface for the simple expense tracker."""

import argparse
from collections import defaultdict
from collections.abc import Sequence
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

from models import Expense
from storage import add_expense, load_expenses

DEFAULT_DATA_FILE = Path.home() / ".expense_tracker" / "expenses.json"


def parse_amount(value: str) -> Decimal:
    """Parse a positive amount with at most two decimal places."""
    try:
        amount = Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError("amount must be a valid number") from error
    if not amount.is_finite() or amount <= 0:
        raise argparse.ArgumentTypeError("amount must be greater than zero")
    if amount.as_tuple().exponent < -2:
        raise argparse.ArgumentTypeError(
            "amount can have at most two decimal places"
        )
    return amount


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for add, list, and summary commands."""
    parser = argparse.ArgumentParser(
        description="Record expenses and review spending totals."
    )
    parser.add_argument(
        "--data-file",
        type=Path,
        default=DEFAULT_DATA_FILE,
        help=f"JSON storage path (default: {DEFAULT_DATA_FILE})",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add_command = commands.add_parser("add", help="record a new expense")
    add_command.add_argument("--description", required=True)
    add_command.add_argument("--amount", type=parse_amount, required=True)
    add_command.add_argument("--category", required=True)
    add_command.add_argument("--date", default=date.today().isoformat())

    commands.add_parser("list", help="list saved expenses")
    commands.add_parser("summary", help="show totals by category")
    return parser


def run(args: argparse.Namespace) -> int:
    """Execute a parsed command and print its result."""
    if args.command == "add":
        expense = Expense(
            id=0,
            description=args.description,
            amount=args.amount,
            category=args.category,
            date=args.date,
        )
        saved = add_expense(args.data_file, expense)
        print(
            f"Added expense #{saved.id}: {saved.description} "
            f"({saved.amount:.2f}, {saved.category}, {saved.date})"
        )
        return 0

    expenses = load_expenses(args.data_file)
    if not expenses:
        print("No expenses recorded.")
        return 0

    if args.command == "list":
        print("ID  DATE        CATEGORY       DESCRIPTION              AMOUNT")
        for expense in expenses:
            print(
                f"{expense.id:<3} {expense.date:<11} "
                f"{expense.category:<14} {expense.description:<24} "
                f"{expense.amount:>8.2f}"
            )
        return 0

    totals: dict[str, Decimal] = defaultdict(Decimal)
    for expense in expenses:
        totals[expense.category] += expense.amount

    print("Spending by category:")
    for category in sorted(totals):
        print(f"{category}: {totals[category]:.2f}")
    print(f"Total: {sum(totals.values(), Decimal('0.00')):.2f}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Parse command-line arguments and run the requested operation."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return run(args)
    except (OSError, TypeError, ValueError) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
