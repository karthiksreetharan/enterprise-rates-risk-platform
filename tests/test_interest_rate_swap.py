from datetime import date

from pytest import raises

from src.common.enums import (
    DayCountConvention,
    FloatingIndex,
    PaymentFrequency,
    PayReceive,
)
from src.products.fixed_leg import FixedLeg
from src.products.floating_leg import FloatingLeg
from src.products.interest_rate_swap import InterestRateSwap
from src.products.trade import Trade


def build_trade():

    return Trade(
        trade_id="IRS001",
        counterparty="Goldman Sachs",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2031, 1, 1),
    )


def build_fixed_leg():

    return FixedLeg(
        notional=10_000_000,
        fixed_rate=0.05,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.PAY,
    )


def build_floating_leg():

    return FloatingLeg(
        notional=10_000_000,
        floating_index=FloatingIndex.SOFR,
        spread=0.0,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.RECEIVE,
    )


def test_swap_creation():

    swap = InterestRateSwap(
        trade=build_trade(),
        fixed_leg=build_fixed_leg(),
        floating_leg=build_floating_leg(),
    )

    assert swap.trade.trade_id == "IRS001"


def test_invalid_pay_receive():

    floating = FloatingLeg(
        notional=10_000_000,
        floating_index=FloatingIndex.SOFR,
        spread=0.0,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.PAY,
    )

    with raises(ValueError):

        InterestRateSwap(
            trade=build_trade(),
            fixed_leg=build_fixed_leg(),
            floating_leg=floating,
        )


def test_invalid_notional():

    floating = FloatingLeg(
        notional=5_000_000,
        floating_index=FloatingIndex.SOFR,
        spread=0.0,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.RECEIVE,
    )

    with raises(ValueError):

        InterestRateSwap(
            trade=build_trade(),
            fixed_leg=build_fixed_leg(),
            floating_leg=floating,
        )