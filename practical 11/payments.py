"""Payment total calculations for the CI log analysis practical."""


def calculate_total(amount: float, fee: float) -> float:
    """Return the payment amount plus its processing fee."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if fee < 0:
        raise ValueError("fee cannot be negative")
    return round(amount + fee, 2)
