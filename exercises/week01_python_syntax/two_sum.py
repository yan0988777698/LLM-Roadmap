"""Rewrite the Two Sum exercise in Python."""


def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the indices of two numbers whose sum equals the target."""
    num_dict: dict[int, int] = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return num_dict[complement], i
        num_dict[num] = i
    return None


def main() -> None:
    """Run repeatable checks for the Two Sum implementation."""
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([1, 2, 3], 99) is None
    print("All tests passed.")


if __name__ == "__main__":
    main()
