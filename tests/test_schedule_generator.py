from datetime import date

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
from src.schedule.schedule_generator import ScheduleGenerator


def build_swap():

    trade = Trade(
        trade_id="IRS001",
        counterparty="ABC Bank",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2031, 1, 1),
    )

    fixed_leg = FixedLeg(
        notional=1_000_000,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.RECEIVE,
        fixed_rate=0.05,
    )

    floating_leg = FloatingLeg(
        notional=1_000_000,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.PAY,
        floating_index=FloatingIndex.SOFR,
        spread=0.0,
    )

    return InterestRateSwap(
        trade=trade,
        fixed_leg=fixed_leg,
        floating_leg=floating_leg,
    )


def build_schedule():

    generator = ScheduleGenerator()
    return generator.generate(build_swap())


def test_schedule_generation():

    schedule = build_schedule()

    assert len(schedule) == 5


def test_schedule_boundaries():

    schedule = build_schedule()

    assert schedule.start_date == date(2026, 1, 1)
    assert schedule.end_date == date(2031, 1, 1)


def test_payment_dates():

    schedule = build_schedule()

    for period in schedule:
        assert period.payment_date == period.accrual_end


def test_schedule_has_no_gaps():

    schedule = build_schedule()

    for previous, current in zip(schedule, schedule[1:]):
        assert previous.accrual_end == current.accrual_start


def test_each_period_is_one_year():

    schedule = build_schedule()

    for period in schedule:
        assert period.accrual_days in (365, 366)