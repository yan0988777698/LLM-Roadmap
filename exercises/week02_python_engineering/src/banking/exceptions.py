"""Domain exceptions for the Week 2 banking package."""


class InvalidAmountError(ValueError):
    """Raised when a deposit or withdrawal amount is not positive."""


class InsufficientFundsError(ValueError):
    """Raised when an account cannot cover a withdrawal."""

