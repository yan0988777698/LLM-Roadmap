"""Domain exceptions for the Week 2 banking package."""


class InvalidAmountError(ValueError):
    """Raised when an initial balance or transaction amount is invalid."""


class InsufficientFundsError(ValueError):
    """Raised when an account cannot cover a withdrawal."""
