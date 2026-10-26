"""Check user story coverage, format, and acceptance criteria completeness."""

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

REQUIREMENT_PATTERN = re.compile(r"^(REQ-\d+):", re.MULTILINE)
STORY_PATTERN = re.compile(r"^##\s+(US-\d+):?.*$", re.MULTILINE)
STORY_TEMPLATE_PATTERN = re.compile(
    r"\*\*As a\*\*\s+.+?,\s+\*\*I want\*\*\s+.+?,\s+"
    r"\*\*so that\*\*\s+.+",
    re.IGNORECASE | re.DOTALL,
)
REQUIREMENT_REFERENCE_PATTERN = re.compile(
    r"\*\*Requirement:\*\*\s*(REQ-\d+)", re.IGNORECASE
)
BDD_PATTERN = re.compile(
    r"^\s*-\s+Given\s+.+\bWhen\s+.+\bThen\s+.+$",
    re.IGNORECASE,
)
MINIMUM_ACCEPTANCE_CRITERIA = 2


@dataclass(frozen=True)
class Story:
    """A user story and its associated source text."""

    identifier: str
    content: str


@dataclass(frozen=True)
class CheckResult:
    """Completeness evaluation details for a set of user stories."""

    checks: tuple[tuple[str, bool, str], ...]

    @property
    def passed(self) -> int:
        """Return the number of checks that passed."""
        return sum(is_passed for _, is_passed, _ in self.checks)

    @property
    def total(self) -> int:
        """Return the number of completeness checks."""
        return len(self.checks)

    @property
    def is_complete(self) -> bool:
        """Return whether every completeness check passed."""
        return self.passed == self.total


def parse_stories(stories_text: str) -> list[Story]:
    """Split Markdown into user stories, each beginning with a level-two heading."""
    matches = list(STORY_PATTERN.finditer(stories_text))
    stories = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(stories_text)
        stories.append(Story(match.group(1), stories_text[match.end():end]))
    return stories


def evaluate_stories(srs_text: str, stories_text: str) -> CheckResult:
    """Evaluate requirement coverage, story format, and testable criteria."""
    requirements = set(REQUIREMENT_PATTERN.findall(srs_text))
    stories = parse_stories(stories_text)

    referenced_requirements = set()
    for story in stories:
        referenced_requirements.update(
            REQUIREMENT_REFERENCE_PATTERN.findall(story.content)
        )
    missing_requirements = sorted(requirements - referenced_requirements)
    unknown_requirements = sorted(referenced_requirements - requirements)
    coverage_passed = bool(requirements) and not missing_requirements and not unknown_requirements
    coverage_details = []
    if missing_requirements:
        coverage_details.append(f"missing {', '.join(missing_requirements)}")
    if unknown_requirements:
        coverage_details.append(f"unknown {', '.join(unknown_requirements)}")
    if not requirements:
        coverage_details.append("no requirements found in the SRS")
    if coverage_passed:
        coverage_details.append(f"all {len(requirements)} requirements are covered")

    malformed_stories = [
        story.identifier
        for story in stories
        if not STORY_TEMPLATE_PATTERN.search(story.content)
    ]
    format_passed = bool(stories) and not malformed_stories
    format_details = (
        "all stories use the As a / I want / so that format"
        if format_passed
        else (
            "no user stories found"
            if not stories
            else "incomplete user story format in "
            + ", ".join(malformed_stories)
        )
    )

    insufficient_criteria = []
    for story in stories:
        valid_criteria = sum(
            bool(BDD_PATTERN.match(line))
            for line in story.content.splitlines()
        )
        if valid_criteria < MINIMUM_ACCEPTANCE_CRITERIA:
            insufficient_criteria.append(
                f"{story.identifier} has {valid_criteria}; "
                f"needs {MINIMUM_ACCEPTANCE_CRITERIA}"
            )
    criteria_passed = bool(stories) and not insufficient_criteria
    criteria_details = (
        "every story has at least two Given/When/Then criteria"
        if criteria_passed
        else (
            "no user stories found"
            if not stories
            else "; ".join(insufficient_criteria)
        )
    )

    return CheckResult(
        checks=(
            ("Requirement coverage", coverage_passed, "; ".join(coverage_details)),
            ("User story format", format_passed, format_details),
            ("Acceptance criteria", criteria_passed, criteria_details),
        )
    )


def main() -> None:
    """Read the SRS and stories, then print a concise completeness report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stories",
        type=Path,
        help="Markdown file containing user stories to evaluate",
    )
    args = parser.parse_args()
    srs_path = Path(__file__).with_name("srs_excerpt.txt")
    result = evaluate_stories(
        srs_path.read_text(encoding="utf-8"),
        args.stories.read_text(encoding="utf-8"),
    )

    percentage = round(result.passed / result.total * 100) if result.total else 0
    print(f"Completeness: {result.passed}/{result.total} checks passed ({percentage}%)")
    for name, passed, details in result.checks:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {details}")
    if not result.is_complete:
        print("Evaluation result: INCOMPLETE - revise the stories and check again.")
    else:
        print("Evaluation result: COMPLETE")


if __name__ == "__main__":
    main()
