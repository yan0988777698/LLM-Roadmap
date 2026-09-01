"""Tests for the Week 2 generator exercise."""

from decimal import Decimal

from banking.generators import iter_amounts_at_least


def test_iter_amounts_at_least_is_lazy_and_filters_values() -> None:
    amounts = [Decimal("10"), Decimal("50"), Decimal("100")]

    result = iter_amounts_at_least(amounts, minimum=Decimal("50"))

    assert iter(result) is result
    assert list(result) == [Decimal("50"), Decimal("100")]

