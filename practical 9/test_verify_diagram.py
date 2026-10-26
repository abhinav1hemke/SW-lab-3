"""Tests for Graphviz ER diagram verification."""

import unittest

from verify_diagram import verify_diagram

VALID_DOT = """
digraph LibraryER {
    LibraryMember [label="{LibraryMember|PK member_id}"];
    Book [label="{Book|PK isbn}"];
    Loan [label="{Loan|PK loan_id}"];
    Reservation [label="{Reservation|PK reservation_id}"];
    LibraryMember -> Loan;
    Book -> Loan;
    LibraryMember -> Reservation;
    Book -> Reservation;
}
"""
VALID_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg">
  <text>LibraryMember</text>
  <text>Book</text>
  <text>Loan</text>
  <text>Reservation</text>
</svg>
"""


class VerifyDiagramTests(unittest.TestCase):
    def test_complete_dot_and_svg_pass(self) -> None:
        results = verify_diagram(VALID_DOT, VALID_SVG)
        self.assertEqual([result.passed for result in results], [True, True])

    def test_missing_relationship_fails_source_check(self) -> None:
        dot_text = VALID_DOT.replace("Book -> Reservation;", "")
        results = verify_diagram(dot_text, VALID_SVG)
        self.assertFalse(results[0].passed)
        self.assertIn("Book -> Reservation", results[0].details)

    def test_missing_entity_label_fails_svg_check(self) -> None:
        svg_text = VALID_SVG.replace("<text>Loan</text>", "")
        results = verify_diagram(VALID_DOT, svg_text)
        self.assertTrue(results[0].passed)
        self.assertFalse(results[1].passed)
        self.assertIn("Loan", results[1].details)

    def test_malformed_svg_is_reported(self) -> None:
        results = verify_diagram(VALID_DOT, "<svg>")
        self.assertFalse(results[1].passed)
        self.assertIn("invalid XML", results[1].details)


if __name__ == "__main__":
    unittest.main()
