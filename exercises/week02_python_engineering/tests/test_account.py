"""Expected behavior for the Account exercise."""

from decimal import Decimal

import pytest

from banking import Account, InsufficientFundsError, InvalidAmountError


def test_deposit_updates_and_returns_balance() -> None:
    account = Account(owner="Alice")

    new_balance = account.deposit(Decimal("100"))

    assert new_balance == Decimal("100")
    assert account.balance == Decimal("100")


@pytest.mark.parametrize("amount", [Decimal("0"), Decimal("-1")])
def test_deposit_rejects_non_positive_amount(amount: Decimal) -> None:
    account = Account(owner="Alice")

    with pytest.raises(InvalidAmountError):
        account.deposit(amount)


def test_withdraw_updates_and_returns_balance() -> None:
    account = Account(owner="Alice", balance=Decimal("100"))

    new_balance = account.withdraw(Decimal("40"))

    assert new_balance == Decimal("60")
    assert account.balance == Decimal("60")


def test_withdraw_rejects_insufficient_funds() -> None:
    account = Account(owner="Alice", balance=Decimal("50"))

    with pytest.raises(InsufficientFundsError):
        account.withdraw(Decimal("60"))
    assert account.balance == Decimal("50")


@pytest.mark.parametrize("balance", ["-1", "NaN", "Infinity", "-Infinity"])
def test_account_rejects_invalid_initial_balance(balance: str) -> None:
    with pytest.raises(InvalidAmountError):
        Account(owner="Alice", balance=Decimal(balance))


@pytest.mark.parametrize("operation", ["deposit", "withdraw"])
@pytest.mark.parametrize("amount", ["0", "-1", "NaN", "Infinity", "-Infinity"])
def test_invalid_operation_keeps_balance(operation: str, amount: str) -> None:
    account = Account(owner="Alice", balance=Decimal("50"))
    with pytest.raises(InvalidAmountError):
        getattr(account, operation)(Decimal(amount))
    assert account.balance == Decimal("50")


def test_withdraw_allows_exact_balance() -> None:
    account = Account(owner="Alice", balance=Decimal("50"))
    assert account.withdraw(Decimal("50")) == Decimal("0")
