"""Generator exercises for transaction-like amounts."""

from collections.abc import Iterable, Iterator
from decimal import Decimal


def iter_amounts_at_least(
    amounts: Iterable[Decimal], minimum: Decimal
) -> Iterator[Decimal]:
    """Yield amounts greater than or equal to the requested minimum."""
    for amount in amounts:
        if amount >= minimum:
            yield amount

