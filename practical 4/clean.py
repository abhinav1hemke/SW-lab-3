"""Create and display a readable invoice from a list of products."""

from collections.abc import Sequence
from dataclasses import dataclass

Product = tuple[str, float, int]


@dataclass(frozen=True)
class Invoice:
    """Store the calculated monetary values for an invoice."""

    subtotal: float
    discount: float
    tax: float
    total: float


PRODUCTS: list[Product] = [
    ("Notebook", 120.0, 2),
    ("Pen pack", 80.0, 1),
    ("Backpack", 300.0, 1),
]
DISCOUNT_THRESHOLD = 500.0
DISCOUNT_RATE = 0.10
TAX_RATE = 0.08


def calculate_invoice(products: Sequence[Product]) -> Invoice:
    """Calculate subtotal, eligible discount, tax, and total for products.

    Each product is a (name, unit price, quantity) tuple. A 10% discount
    applies when the subtotal is at least INR 500. Tax is 8% of the amount
    after discount.
    """
    subtotal = sum(unit_price * quantity for _, unit_price, quantity in products)
    discount = subtotal * DISCOUNT_RATE if subtotal >= DISCOUNT_THRESHOLD else 0.0
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * TAX_RATE
    total = discounted_subtotal + tax

    return Invoice(
        subtotal=subtotal,
        discount=discount,
        tax=tax,
        total=total,
    )


def display_invoice(products: Sequence[Product], invoice: Invoice) -> None:
    """Print an itemized invoice and its calculated totals."""
    print("INVOICE")
    for name, unit_price, quantity in products:
        line_total = unit_price * quantity
        print(f"{name} x {quantity}: INR {line_total:.2f}")
    print(f"Subtotal: INR {invoice.subtotal:.2f}")
    print(f"Discount: INR {invoice.discount:.2f}")
    print(f"Tax: INR {invoice.tax:.2f}")
    print(f"Total: INR {invoice.total:.2f}")


def main() -> None:
    """Calculate and print the sample invoice."""
    invoice = calculate_invoice(PRODUCTS)
    display_invoice(PRODUCTS, invoice)


if __name__ == "__main__":
    main()
