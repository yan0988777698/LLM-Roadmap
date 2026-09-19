"""Account model used to practice dataclasses, typing, and exceptions."""

from dataclasses import dataclass, field
from decimal import Decimal

from .exceptions import InsufficientFundsError, InvalidAmountError


@dataclass(slots=True)
class Account:
    """Represent a simple bank account with a non-negative balance."""

    owner: str
    balance: Decimal = field(default_factory=lambda: Decimal("0"))

    def __post_init__(self) -> None:
        if not self.balance.is_finite() or self.balance < 0:
            raise InvalidAmountError("Initial balance must be finite and non-negative")

    def deposit(self, amount: Decimal) -> Decimal:
        """Deposit a positive amount and return the new balance."""
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Decimal) -> Decimal:
        """Withdraw an available positive amount and return the new balance."""
        self._validate_amount(amount)
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        return self.balance

    @staticmethod
    def _validate_amount(amount: Decimal) -> None:
        """Reject non-finite and non-positive Decimal amounts."""
        if not amount.is_finite() or amount <= 0:
            raise InvalidAmountError("Amount must be finite and positive")
