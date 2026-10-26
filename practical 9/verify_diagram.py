"""Verify that the ER diagram source and its rendered SVG meet requirements."""

import argparse
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ENTITY_NAMES = ("LibraryMember", "Book", "Loan", "Reservation")
RELATIONSHIPS = (
    ("LibraryMember", "Loan"),
    ("Book", "Loan"),
    ("LibraryMember", "Reservation"),
    ("Book", "Reservation"),
)


@dataclass(frozen=True)
class Verification:
    """One named verification result."""

    name: str
    passed: bool
    details: str


def verify_diagram(dot_text: str, svg_text: str) -> tuple[Verification, ...]:
    """Check required entities and relationships in DOT and entity labels in SVG."""
    declared_entities = {
        name
        for name in ENTITY_NAMES
        if re.search(rf"^\s*{re.escape(name)}\s*\[", dot_text, re.MULTILINE)
    }
    missing_entities = sorted(set(ENTITY_NAMES) - declared_entities)
    missing_relationships = [
        f"{start} -> {end}"
        for start, end in RELATIONSHIPS
        if not re.search(
            rf"\b{re.escape(start)}\s*->\s*{re.escape(end)}\b", dot_text
        )
    ]
    source_passed = not missing_entities and not missing_relationships
    source_details = "all 4 entities and 4 relationships are declared"
    if not source_passed:
        problems = []
        if missing_entities:
            problems.append(f"missing entities: {', '.join(missing_entities)}")
        if missing_relationships:
            problems.append(
                f"missing relationships: {', '.join(missing_relationships)}"
            )
        source_details = "; ".join(problems)

    try:
        svg_root = ET.fromstring(svg_text)
    except ET.ParseError as error:
        return (
            Verification("DOT source", source_passed, source_details),
            Verification("Rendered SVG", False, f"invalid XML: {error}"),
        )

    is_svg = svg_root.tag.rsplit("}", maxsplit=1)[-1] == "svg"
    svg_visible_text = " ".join(
        text.strip()
        for text in svg_root.itertext()
        if text and text.strip()
    )
    missing_rendered_entities = [
        name for name in ENTITY_NAMES if name not in svg_visible_text
    ]
    svg_passed = is_svg and not missing_rendered_entities
    if not is_svg:
        svg_details = "rendered file root element is not SVG"
    elif missing_rendered_entities:
        svg_details = (
            "missing rendered entity labels: "
            + ", ".join(missing_rendered_entities)
        )
    else:
        svg_details = "valid SVG includes all 4 entity labels"

    return (
        Verification("DOT source", source_passed, source_details),
        Verification("Rendered SVG", svg_passed, svg_details),
    )


def main() -> None:
    """Read the DOT and SVG files and print their verification results."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dot",
        type=Path,
        default=Path(__file__).with_name("library_er.dot"),
        help="Graphviz DOT source (defaults to library_er.dot)",
    )
    parser.add_argument(
        "--svg",
        type=Path,
        default=Path(__file__).with_name("library_er.svg"),
        help="rendered SVG diagram (defaults to library_er.svg)",
    )
    args = parser.parse_args()
    results = verify_diagram(
        args.dot.read_text(encoding="utf-8"),
        args.svg.read_text(encoding="utf-8"),
    )
    print("Diagram verification:")
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.name}: {result.details}")
    if not all(result.passed for result in results):
        raise SystemExit(1)
    print("Verification result: PASS")


if __name__ == "__main__":
    main()
