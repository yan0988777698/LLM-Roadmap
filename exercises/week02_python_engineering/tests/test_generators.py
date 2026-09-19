"""Tests for the Week 2 generator exercise."""

from decimal import Decimal

from banking.generators import iter_amounts_at_least


def test_iter_amounts_at_least_is_lazy_and_filters_values() -> None:
    amounts = [Decimal("10"), Decimal("50"), Decimal("100")]

    result = iter_amounts_at_least(amounts, minimum=Decimal("50"))

    assert iter(result) is result
    assert list(result) == [Decimal("50"), Decimal("100")]


def test_generator_consumes_input_only_as_needed() -> None:
    visited = []

    def source():
        for value in ("10", "50", "100"):
            visited.append(value)
            yield Decimal(value)

    result = iter_amounts_at_least(source(), minimum=Decimal("50"))
    assert visited == []
    assert next(result) == Decimal("50")
    assert visited == ["10", "50"]
    assert list(result) == [Decimal("100")]
    assert list(result) == []
