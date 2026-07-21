from datetime import date

from pytest import raises

from src.common.enums import CashFlowType
from src.products.cashflow import CashFlow


def test_cashflow_creation():

    cf = CashFlow(
        payment_date=date(2027, 1, 1),
        accrual_start=date(2026, 1, 1),
        accrual_end=date(2027, 1, 1),
        year_fraction=1.0,
        notional=10_000_000,
        rate=0.05,
        amount=500_000,
        currency="USD",
        cashflow_type=CashFlowType.FIXED,
    )

    assert cf.amount == 500_000
    assert cf.notional == 10_000_000
    assert cf.rate == 0.05
    assert cf.currency == "USD"
    assert cf.cashflow_type == CashFlowType.FIXED


def test_invalid_dates():

    with raises(ValueError):

        CashFlow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2027, 1, 1),
            accrual_end=date(2026, 1, 1),
            year_fraction=1.0,
            notional=1_000_000,
            rate=0.05,
            amount=100,
            currency="USD",
            cashflow_type=CashFlowType.FIXED,
        )


def test_invalid_year_fraction():

    with raises(ValueError):

        CashFlow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2026, 1, 1),
            accrual_end=date(2027, 1, 1),
            year_fraction=0.0,
            notional=1_000_000,
            rate=0.05,
            amount=100,
            currency="USD",
            cashflow_type=CashFlowType.FIXED,
        )


def test_invalid_notional():

    with raises(ValueError):

        CashFlow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2026, 1, 1),
            accrual_end=date(2027, 1, 1),
            year_fraction=1.0,
            notional=0,
            rate=0.05,
            amount=100,
            currency="USD",
            cashflow_type=CashFlowType.FIXED,
        )


def test_empty_currency():

    with raises(ValueError):

        CashFlow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2026, 1, 1),
            accrual_end=date(2027, 1, 1),
            year_fraction=1.0,
            notional=1_000_000,
            rate=0.05,
            amount=100,
            currency="",
            cashflow_type=CashFlowType.FIXED,
        )