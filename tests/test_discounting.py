from datetime import date

from src.cashflows.cashflow_generator import CashFlowGenerator
from src.common.enums import (
    CashFlowType,
    DayCountConvention,
    FloatingIndex,
    PayReceive,
    PaymentFrequency,
)
from src.curves.bootstrapper import Bootstrapper
from src.market_data.market_instrument import MarketInstrument
from src.market_data.market_quote_collection import MarketQuoteCollection
from src.pricing.discounting import Discounting
from src.products.fixed_leg import FixedLeg
from src.products.floating_leg import FloatingLeg
from src.products.interest_rate_swap import InterestRateSwap
from src.products.trade import Trade
from src.schedule.schedule_generator import ScheduleGenerator


def build_curve():

    quotes = MarketQuoteCollection()

    quotes.add(
        MarketInstrument("Deposit", "1M", 0.048)
    )

    quotes.add(
        MarketInstrument("Deposit", "3M", 0.050)
    )

    quotes.add(
        MarketInstrument("Deposit", "6M", 0.052)
    )

    quotes.add(
        MarketInstrument("Deposit", "1Y", 0.055)
    )

    quotes.add(
        MarketInstrument("Deposit", "2Y", 0.057)
    )

    quotes.add(
        MarketInstrument("Deposit", "3Y", 0.059)
    )

    return Bootstrapper(
        date(2026, 1, 1),
        quotes,
    ).build()


def build_swap():

    trade = Trade(
        trade_id="IRS001",
        counterparty="ABC Bank",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2029, 1, 1),   # 3Y swap
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


def test_discount_cashflows():

    curve = build_curve()

    swap = build_swap()

    schedule = ScheduleGenerator().generate(
        swap
    )

    cashflows = CashFlowGenerator().generate(
        swap,
        schedule,
    )

    discounted = Discounting().discount(
        cashflows,
        curve,
    )

    assert len(discounted) == len(cashflows)

    for dcf in discounted:

        assert dcf.discount_factor > 0.0
        assert dcf.discount_factor <= 1.0

        assert dcf.present_value > 0.0
        assert dcf.present_value <= dcf.amount

        assert dcf.cashflow.cashflow_type == CashFlowType.FIXED