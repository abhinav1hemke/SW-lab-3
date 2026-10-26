"""Verify the reported payment calculation cause against the corrected code."""

from pathlib import Path

from analyze_log import analyze_log
from payments import calculate_total


def verify_cause() -> tuple[bool, str]:
    """Confirm the log diagnosis by reproducing expected behavior after the fix."""
    log_path = Path(__file__).with_name("build.log")
    report = analyze_log(log_path.read_text(encoding="utf-8"))
    if "processing fee appears to have been added twice" not in report:
        return False, "The log did not confirm the duplicate-fee diagnosis."

    actual_total = calculate_total(100.00, 8.00)
    expected_total = 108.00
    if actual_total != expected_total:
        return (
            False,
            (
                f"Corrected calculation returned {actual_total:.2f}; "
                f"expected {expected_total:.2f}."
            ),
        )
    return (
        True,
        (
            "Probable cause verified: the historical failure added the fee "
            "twice; the corrected code returns 108.00 for amount 100.00 "
            "and fee 8.00."
        ),
    )


if __name__ == "__main__":
    verified, message = verify_cause()
    print(message)
    if not verified:
        raise SystemExit(1)
