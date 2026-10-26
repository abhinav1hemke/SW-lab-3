"""Validated data model for the simple expense tracker."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Expense:
    """One expense with a positive amount and ISO-format calendar date."""

    id: int
    description: str
    amount: Decimal
    category: str
    date: str

    def __post_init__(self) -> None:
        """Reject invalid values when an expense is created."""
        if self.id < 0:
            raise ValueError("expense ID cannot be negative")
        if not self.description.strip():
            raise ValueError("description must not be empty")
        if not self.category.strip():
            raise ValueError("category must not be empty")

        try:
            amount = Decimal(self.amount)
        except (InvalidOperation, TypeError, ValueError) as error:
            raise ValueError("amount must be a valid positive number") from error
        if not amount.is_finite() or amount <= 0:
            raise ValueError("amount must be a valid positive number")
        if amount.as_tuple().exponent < -2:
            raise ValueError("amount can have at most two decimal places")
        object.__setattr__(self, "amount", amount)

        try:
            parsed_date = date.fromisoformat(self.date)
        except ValueError as error:
            raise ValueError("date must use YYYY-MM-DD format") from error
        if parsed_date.isoformat() != self.date:
            raise ValueError("date must use YYYY-MM-DD format")

    def to_dict(self) -> dict[str, int | str]:
        """Return a JSON-compatible representation of this expense."""
        return {
            "id": self.id,
            "description": self.description.strip(),
            "amount": format(self.amount, ".2f"),
            "category": self.category.strip(),
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Expense":
        """Create an expense from a saved JSON record."""
        try:
            expense_id = data["id"]
            description = data["description"]
            amount = data["amount"]
            category = data["category"]
            expense_date = data["date"]
            if (
                not isinstance(expense_id, int)
                or isinstance(expense_id, bool)
                or not isinstance(description, str)
                or not isinstance(amount, str)
                or not isinstance(category, str)
                or not isinstance(expense_date, str)
            ):
                raise TypeError("expense record has invalid field types")
            return cls(
                id=expense_id,
                description=description,
                amount=Decimal(amount),
                category=category,
                date=expense_date,
            )
        except KeyError as error:
            raise ValueError(
                f"expense record is missing field {error.args[0]!r}"
            ) from error
        except InvalidOperation as error:
            raise ValueError("expense record has an invalid amount") from error
