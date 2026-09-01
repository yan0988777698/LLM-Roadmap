"""Account model used to practice dataclasses, typing, and exceptions."""

from dataclasses import dataclass, field
from decimal import Decimal

from .exceptions import InsufficientFundsError, InvalidAmountError


@dataclass(slots=True)
class Account:
    """Represent a simple bank account with a non-negative balance."""

    owner: str
    balance: Decimal = field(default_factory=lambda: Decimal("0"))

    def deposit(self, amount: Decimal) -> Decimal:
        """Deposit a positive amount and return the new balance."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Decimal) -> Decimal:
        """Withdraw an available positive amount and return the new balance."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        return self.balance

    @staticmethod
    def _validate_amount(amount: Decimal) -> None:
        """Raise InvalidAmountError when the amount is not positive."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
