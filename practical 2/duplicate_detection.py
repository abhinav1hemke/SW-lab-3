"""Compare straightforward and optimized duplicate detection."""

from __future__ import annotations

import argparse
import statistics
import time
from collections.abc import Callable, Sequence


def find_duplicates_naive(values: Sequence[int]) -> list[int]:
    """Return each repeated integer once, in order of its first occurrence."""
    duplicates: list[int] = []

    for index, value in enumerate(values):
        if value in duplicates:
            continue
        for later_value in values[index + 1 :]:
            if value == later_value:
                duplicates.append(value)
                break

    return duplicates


def find_duplicates_optimized(values: Sequence[int]) -> list[int]:
    """Find repeated integers in average O(n) time using sets."""
    seen: set[int] = set()
    duplicate_values: set[int] = set()
    duplicates: list[int] = []

    for value in values:
        if value in seen:
            if value not in duplicate_values:
                duplicate_values.add(value)
                duplicates.append(value)
        else:
            seen.add(value)

    return duplicates


def build_dataset(size: int) -> list[int]:
    """Create a deterministic dataset where every other value is repeated."""
    if size < 0:
        raise ValueError("size must be zero or greater")
    return list(range(size)) + list(range(0, size, 2))


def median_runtime(
    function: Callable[[Sequence[int]], list[int]],
    values: Sequence[int],
    repeats: int,
) -> float:
    """Return the median elapsed time in seconds over the requested repeats."""
    measurements: list[float] = []
    for _ in range(repeats):
        start = time.perf_counter()
        function(values)
        measurements.append(time.perf_counter() - start)
    return statistics.median(measurements)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare naive and optimized duplicate detection."
    )
    parser.add_argument(
        "--size",
        type=int,
        default=5_000,
        help="number of unique values before duplicates are added (default: 5000)",
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=3,
        help="number of benchmark runs used to calculate the median (default: 3)",
    )
    args = parser.parse_args()

    if args.size < 0:
        parser.error("--size must be zero or greater")
    if args.repeats < 1:
        parser.error("--repeats must be at least 1")

    values = build_dataset(args.size)
    naive_result = find_duplicates_naive(values)
    optimized_result = find_duplicates_optimized(values)
    if naive_result != optimized_result:
        raise RuntimeError("The two implementations returned different results.")

    naive_time = median_runtime(find_duplicates_naive, values, args.repeats)
    optimized_time = median_runtime(find_duplicates_optimized, values, args.repeats)
    speedup = naive_time / optimized_time if optimized_time else float("inf")

    print(f"Input values: {len(values)} ({args.size} unique values)")
    print(f"Duplicates found: {len(optimized_result)}")
    print(f"Naive median: {naive_time:.6f} seconds")
    print(f"Optimized median: {optimized_time:.6f} seconds")
    print(f"Measured speedup: {speedup:.2f}x")


if __name__ == "__main__":
    main()
