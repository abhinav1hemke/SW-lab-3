"""Validated sample application after static analysis fixes."""

import ast
import os
from collections.abc import Mapping

ENVIRONMENT_SETTING_NAME = "PRACTICAL6_API_TOKEN"


def parse_user_record(record: str) -> dict[str, object]:
    """Parse a dictionary literal without executing arbitrary code."""
    try:
        parsed_record = ast.literal_eval(record)
    except (SyntaxError, ValueError) as error:
        raise ValueError("record must be a valid dictionary literal") from error

    if not isinstance(parsed_record, dict):
        raise TypeError("record must contain a dictionary")
    return parsed_record


def get_api_token(
    environment: Mapping[str, str] | None = None,
) -> str:
    """Read the API token from the environment, never from source code."""
    source = os.environ if environment is None else environment
    token = source.get(ENVIRONMENT_SETTING_NAME)
    if not token:
        raise ValueError(
            f"Set the {ENVIRONMENT_SETTING_NAME} environment variable"
        )
    return token


def calculate_discount(price: float, discount_percent: float) -> float:
    """Return the price after applying a percentage discount."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


if __name__ == "__main__":
    print(f"Discounted price: {calculate_discount(100, 10):.2f}")
