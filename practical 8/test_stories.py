"""Tests for the user story completeness checker."""

import unittest
from pathlib import Path

from check_stories import evaluate_stories

PRACTICAL_DIRECTORY = Path(__file__).parent
SRS_TEXT = (PRACTICAL_DIRECTORY / "srs_excerpt.txt").read_text(encoding="utf-8")
DRAFT_TEXT = (PRACTICAL_DIRECTORY / "draft1.md").read_text(encoding="utf-8")
REVISED_TEXT = (PRACTICAL_DIRECTORY / "revised_stories.md").read_text(
    encoding="utf-8"
)


class EvaluateStoriesTests(unittest.TestCase):
    def test_draft_one_is_incomplete(self) -> None:
        result = evaluate_stories(SRS_TEXT, DRAFT_TEXT)
        self.assertFalse(result.is_complete)
        self.assertEqual(result.passed, 1)
        self.assertIn("missing REQ-03", result.checks[0][2])
        self.assertIn("US-01 has 1", result.checks[2][2])
        self.assertIn("US-02 has 0", result.checks[2][2])

    def test_revised_stories_are_complete(self) -> None:
        result = evaluate_stories(SRS_TEXT, REVISED_TEXT)
        self.assertTrue(result.is_complete)
        self.assertEqual(result.passed, 3)

    def test_missing_user_story_fails_format_and_criteria_checks(self) -> None:
        result = evaluate_stories(SRS_TEXT, "# No stories yet\n")
        self.assertFalse(result.is_complete)
        self.assertFalse(result.checks[1][1])
        self.assertFalse(result.checks[2][1])

    def test_unknown_requirement_reference_fails_coverage(self) -> None:
        stories = REVISED_TEXT.replace("REQ-03", "REQ-99")
        result = evaluate_stories(SRS_TEXT, stories)
        self.assertFalse(result.checks[0][1])
        self.assertIn("missing REQ-03", result.checks[0][2])
        self.assertIn("unknown REQ-99", result.checks[0][2])


if __name__ == "__main__":
    unittest.main()
