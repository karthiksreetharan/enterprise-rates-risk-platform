from pytest import raises

from src.common.enums import (
    DayCountConvention,
    PaymentFrequency,
    PayReceive,
)
from src.products.fixed_leg import FixedLeg


def test_fixed_leg_creation():

    leg = FixedLeg(
        notional=10_000_000,
        fixed_rate=0.05,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.PAY,
    )

    assert leg.fixed_rate == 0.05
    assert leg.notional == 10_000_000


def test_invalid_notional():

    with raises(ValueError):

        FixedLeg(
            notional=-100,
            fixed_rate=0.05,
            payment_frequency=PaymentFrequency.ANNUAL,
            day_count=DayCountConvention.ACT_365,
            pay_receive=PayReceive.PAY,
        )


def test_invalid_rate():

    with raises(ValueError):

        FixedLeg(
            notional=1000,
            fixed_rate=-0.01,
            payment_frequency=PaymentFrequency.ANNUAL,
            day_count=DayCountConvention.ACT_365,
            pay_receive=PayReceive.PAY,
        )