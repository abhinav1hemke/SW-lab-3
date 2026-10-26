"""Analyze a CI log for test failures and write a probable-cause report."""

import argparse
import re
from pathlib import Path

TOTAL_MISMATCH_PATTERN = re.compile(
    r"expected total\s+(?P<expected>\d+(?:\.\d+)?)\s+but got\s+"
    r"(?P<actual>\d+(?:\.\d+)?)\s+\(amount=(?P<amount>\d+(?:\.\d+)?), "
    r"fee=(?P<fee>\d+(?:\.\d+)?)\)",
    re.IGNORECASE,
)
FAILED_TEST_PATTERN = re.compile(r"FAIL:\s+([^\s]+)")
TRACEBACK_PATTERN = re.compile(r'File "([^"]+)", line (\d+)')


def analyze_log(log_text: str) -> str:
    """Create a concise report from a test-failure log."""
    failed_test_match = FAILED_TEST_PATTERN.search(log_text)
    traceback_match = TRACEBACK_PATTERN.search(log_text)
    mismatch_match = TOTAL_MISMATCH_PATTERN.search(log_text)
    failed_test = failed_test_match.group(1) if failed_test_match else "Not identified"
    source_location = (
        f"{Path(traceback_match.group(1)).name}:{traceback_match.group(2)}"
        if traceback_match
        else "Not identified"
    )

    if mismatch_match:
        expected = float(mismatch_match.group("expected"))
        actual = float(mismatch_match.group("actual"))
        amount = float(mismatch_match.group("amount"))
        fee = float(mismatch_match.group("fee"))
        if abs(actual - expected - fee) < 0.001:
            cause = (
                "The processing fee appears to have been added twice. "
                f"For amount {amount:.2f} and fee {fee:.2f}, expected "
                f"{expected:.2f}, but the failing run returned {actual:.2f}."
            )
        else:
            cause = (
                f"The payment total differs from expected {expected:.2f}: "
                f"the failing run returned {actual:.2f}."
            )
    else:
        cause = (
            "The log does not contain a recognized payment-total mismatch; "
            "inspect the failed test and traceback manually."
        )

    return "\n".join(
        [
            "# CI Build Log Analysis",
            "",
            f"- **Failed test:** `{failed_test}`",
            f"- **Failure location:** `{source_location}`",
            f"- **Probable cause:** {cause}",
            (
                "- **Recommended check:** Compare the payment total calculation "
                "with the requirement to include the processing fee exactly once."
            ),
        ]
    ) + "\n"


def main() -> None:
    """Analyze the requested log and print and save the report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "log_file",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("build.log"),
        help="CI build log to analyze (defaults to build.log)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("analysis_report.md"),
        help="Markdown report path (defaults to analysis_report.md)",
    )
    args = parser.parse_args()
    report = analyze_log(args.log_file.read_text(encoding="utf-8"))
    args.output.write_text(report, encoding="utf-8")
    print(report, end="")
    print(f"Report saved to {args.output.name}")


if __name__ == "__main__":
    main()
