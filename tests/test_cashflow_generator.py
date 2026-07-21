from datetime import date

from src.cashflows.cashflow_generator import CashFlowGenerator
from src.common.enums import (
    CashFlowType,
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
        counterparty="ABC",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2031, 1, 1),
    )

    fixed_leg = FixedLeg(
        notional=1_000_000,
        fixed_rate=0.05,
        payment_frequency=PaymentFrequency.ANNUAL,
        day_count=DayCountConvention.ACT_365,
        pay_receive=PayReceive.RECEIVE,
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


def test_generate_cashflows():

    swap = build_swap()

    schedule = ScheduleGenerator().generate(swap)

    cashflows = CashFlowGenerator().generate(
        swap,
        schedule,
    )

    assert len(cashflows) == 5

    cf = cashflows[0]

    assert cf.payment_date == date(2027, 1, 1)
    assert cf.notional == 1_000_000
    assert cf.rate == 0.05
    assert cf.amount == 50_000.0
    assert cf.cashflow_type == CashFlowType.FIXED