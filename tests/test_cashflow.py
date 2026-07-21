from datetime import date

from pytest import raises

from src.products.cashflow import Cashflow


def test_cashflow_creation():

    cf = Cashflow(
        payment_date=date(2027, 1, 1),
        accrual_start=date(2026, 1, 1),
        accrual_end=date(2027, 1, 1),
        year_fraction=1.0,
        amount=500000,
    )

    assert cf.amount == 500000


def test_invalid_dates():

    with raises(ValueError):

        Cashflow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2027, 1, 1),
            accrual_end=date(2026, 1, 1),
            year_fraction=1.0,
            amount=100,
        )


def test_invalid_year_fraction():

    with raises(ValueError):

        Cashflow(
            payment_date=date(2027, 1, 1),
            accrual_start=date(2026, 1, 1),
            accrual_end=date(2027, 1, 1),
            year_fraction=0.0,
            amount=100,
        )