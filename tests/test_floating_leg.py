from pytest import raises

from src.common.enums import (
    DayCountConvention,
    FloatingIndex,
    PaymentFrequency,
    PayReceive,
)
from src.products.floating_leg import FloatingLeg


def test_floating_leg_creation():

    leg = FloatingLeg(
        notional=5_000_000,
        floating_index=FloatingIndex.SOFR,
        spread=0.001,
        payment_frequency=PaymentFrequency.QUARTERLY,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.RECEIVE,
    )

    assert leg.notional == 5_000_000
    assert leg.spread == 0.001
    assert leg.floating_index == FloatingIndex.SOFR


def test_invalid_notional():

    with raises(ValueError):

        FloatingLeg(
            notional=-1,
            floating_index=FloatingIndex.SOFR,
            spread=0.0,
            payment_frequency=PaymentFrequency.QUARTERLY,
            day_count=DayCountConvention.ACT_365,
            pay_receive=PayReceive.RECEIVE,
        )


def test_invalid_spread_type():

    with raises(TypeError):

        FloatingLeg(
            notional=1_000_000,
            floating_index=FloatingIndex.SOFR,
            spread="abc",
            payment_frequency=PaymentFrequency.QUARTERLY,
            day_count=DayCountConvention.ACT_365,
            pay_receive=PayReceive.RECEIVE,
        )