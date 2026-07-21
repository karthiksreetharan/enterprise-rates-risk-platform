from datetime import date

import pytest

from src.common.enums import CashFlowType
from src.products.cashflow import CashFlow
from src.products.discounted_cashflow import DiscountedCashFlow


def build_cashflow():

    return CashFlow(
        payment_date=date(2027, 1, 1),
        accrual_start=date(2026, 1, 1),
        accrual_end=date(2027, 1, 1),
        year_fraction=1.0,
        notional=1_000_000,
        rate=0.05,
        amount=50_000,
        currency="USD",
        cashflow_type=CashFlowType.FIXED,
    )


def test_discounted_cashflow_creation():

    dcf = DiscountedCashFlow(
        cashflow=build_cashflow(),
        discount_factor=0.95,
        present_value=47_500,
    )

    assert dcf.discount_factor == 0.95
    assert dcf.present_value == 47_500
    assert dcf.amount == 50_000
    assert dcf.currency == "USD"


def test_invalid_discount_factor():

    with pytest.raises(ValueError):

        DiscountedCashFlow(
            cashflow=build_cashflow(),
            discount_factor=1.5,
            present_value=100,
        )