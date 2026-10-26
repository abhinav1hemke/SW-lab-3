"""Tests for CI log analysis and verified payment behavior."""

import unittest
from pathlib import Path

from analyze_log import analyze_log
from verify_cause import verify_cause

BUILD_LOG = Path(__file__).with_name("build.log").read_text(encoding="utf-8")


class AnalyzeLogTests(unittest.TestCase):
    def test_reports_failure_and_duplicate_fee_cause(self) -> None:
        report = analyze_log(BUILD_LOG)
        self.assertIn("test_adds_processing_fee_once", report)
        self.assertIn("test_payments.py:10", report)
        self.assertIn("processing fee appears to have been added twice", report)
        self.assertIn("expected 108.00", report)
        self.assertIn("returned 116.00", report)

    def test_unrecognized_log_recommends_manual_inspection(self) -> None:
        report = analyze_log("CI job failed without test details.")
        self.assertIn("inspect the failed test and traceback manually", report)

    def test_probable_cause_is_verified_against_fixed_code(self) -> None:
        verified, message = verify_cause()
        self.assertTrue(verified)
        self.assertIn("returns 108.00", message)


if __name__ == "__main__":
    unittest.main()
