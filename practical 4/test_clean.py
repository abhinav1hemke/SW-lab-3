import unittest

from clean import calculate_invoice


class CalculateInvoiceTests(unittest.TestCase):
    def test_calculates_discount_tax_and_total(self) -> None:
        invoice = calculate_invoice(
            [
                ("Notebook", 120.0, 2),
                ("Pen pack", 80.0, 1),
                ("Backpack", 300.0, 1),
            ]
        )
        self.assertEqual(invoice.subtotal, 620.0)
        self.assertEqual(invoice.discount, 62.0)
        self.assertAlmostEqual(invoice.tax, 44.64)
        self.assertAlmostEqual(invoice.total, 602.64)

    def test_does_not_apply_discount_below_threshold(self) -> None:
        invoice = calculate_invoice([("Pencil", 10.0, 2)])
        self.assertEqual(invoice.subtotal, 20.0)
        self.assertEqual(invoice.discount, 0.0)
        self.assertAlmostEqual(invoice.tax, 1.6)
        self.assertAlmostEqual(invoice.total, 21.6)

    def test_applies_discount_at_exact_threshold(self) -> None:
        invoice = calculate_invoice([("Bag", 500.0, 1)])
        self.assertEqual(invoice.discount, 50.0)
        self.assertAlmostEqual(invoice.tax, 36.0)
        self.assertAlmostEqual(invoice.total, 486.0)

    def test_empty_product_list_has_zero_totals(self) -> None:
        invoice = calculate_invoice([])
        self.assertEqual(invoice.subtotal, 0.0)
        self.assertEqual(invoice.discount, 0.0)
        self.assertEqual(invoice.tax, 0.0)
        self.assertEqual(invoice.total, 0.0)


if __name__ == "__main__":
    unittest.main()
