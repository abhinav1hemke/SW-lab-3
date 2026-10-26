"""Tests for expense validation, JSON storage, and CLI behavior."""

import contextlib
import io
import json
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from cli import main
from models import Expense
from storage import add_expense, load_expenses, save_expenses


class ExpenseModelTests(unittest.TestCase):
    def test_valid_expense_is_normalized_when_saved(self) -> None:
        expense = Expense(
            id=1,
            description="  Lunch  ",
            amount=Decimal("12.50"),
            category=" Food ",
            date="2026-10-27",
        )
        self.assertEqual(expense.to_dict()["description"], "Lunch")
        self.assertEqual(expense.to_dict()["category"], "Food")
        self.assertEqual(expense.to_dict()["amount"], "12.50")

    def test_rejects_invalid_amounts(self) -> None:
        for amount in (Decimal(0), Decimal(-1), Decimal("1.234")):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                Expense(1, "Lunch", amount, "Food", "2026-10-27")

    def test_rejects_empty_fields_and_invalid_date(self) -> None:
        for description, category, expense_date in (
            (" ", "Food", "2026-10-27"),
            ("Lunch", " ", "2026-10-27"),
            ("Lunch", "Food", "27-10-2026"),
        ):
            with self.subTest(date=expense_date), self.assertRaises(ValueError):
                Expense(1, description, Decimal("1.00"), category, expense_date)


class ExpenseStorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temporary_directory.name) / "data" / "expenses.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_missing_file_loads_as_empty_list(self) -> None:
        self.assertEqual(load_expenses(self.data_file), [])

    def test_add_assigns_incrementing_ids_and_persists(self) -> None:
        first = Expense(0, "Lunch", Decimal("12.50"), "Food", "2026-10-27")
        second = Expense(0, "Bus", Decimal("2.75"), "Travel", "2026-10-27")
        self.assertEqual(add_expense(self.data_file, first).id, 1)
        self.assertEqual(add_expense(self.data_file, second).id, 2)
        self.assertEqual([item.description for item in load_expenses(self.data_file)],
                         ["Lunch", "Bus"])

    def test_invalid_json_is_reported(self) -> None:
        self.data_file.parent.mkdir(parents=True)
        self.data_file.write_text("{broken", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            load_expenses(self.data_file)

    def test_save_and_load_empty_expenses(self) -> None:
        save_expenses(self.data_file, [])
        self.assertEqual(load_expenses(self.data_file), [])
        self.assertEqual(json.loads(self.data_file.read_text())["expenses"], [])


class ExpenseCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temporary_directory.name) / "expenses.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def run_cli(self, *arguments: str) -> str:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(
                main(["--data-file", str(self.data_file), *arguments]),
                0,
            )
        return output.getvalue()

    def test_add_uses_today_by_default(self) -> None:
        output = self.run_cli(
            "add",
            "--description", "Lunch",
            "--amount", "12.50",
            "--category", "Food",
        )
        self.assertIn("Added expense #1", output)
        self.assertEqual(load_expenses(self.data_file)[0].date, date.today().isoformat())

    def test_list_and_summary_show_saved_expenses(self) -> None:
        self.run_cli(
            "add",
            "--description", "Lunch",
            "--amount", "12.50",
            "--category", "Food",
        )
        self.run_cli(
            "add",
            "--description", "Dinner",
            "--amount", "7.50",
            "--category", "Food",
        )
        self.assertIn("Lunch", self.run_cli("list"))
        summary = self.run_cli("summary")
        self.assertIn("Food: 20.00", summary)
        self.assertIn("Total: 20.00", summary)

    def test_empty_list_and_summary_are_reported(self) -> None:
        self.assertEqual(self.run_cli("list"), "No expenses recorded.\n")
        self.assertEqual(self.run_cli("summary"), "No expenses recorded.\n")

    def test_invalid_amount_is_rejected_by_cli(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(
            SystemExit
        ) as error:
            main(
                [
                    "--data-file",
                    str(self.data_file),
                    "add",
                    "--description",
                    "Lunch",
                    "--amount",
                    "-1",
                    "--category",
                    "Food",
                ]
            )
        self.assertEqual(error.exception.code, 2)
        self.assertFalse(self.data_file.exists())


if __name__ == "__main__":
    unittest.main()
