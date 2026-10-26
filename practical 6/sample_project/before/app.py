"""Intentionally flawed sample application for Practical 6."""

import json

api_token = "lab-demo-token-not-a-real-credential"


def parse_user_record(record: str) -> object:
    """Parse a record using an intentionally unsafe implementation."""
    return eval(record)


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate a discount using an intentionally incorrect divisor."""
    return price - (price * discount_percent / 10)


if __name__ == "__main__":
    print(f"Discounted price: {calculate_discount(100, 10):.2f}")
