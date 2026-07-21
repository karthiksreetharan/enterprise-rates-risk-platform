from datetime import date

from src.common.enums import (
    DayCountConvention,
    FloatingIndex,
    PayReceive,
    PaymentFrequency,
)
from src.curves.bootstrapper import Bootstrapper
from src.market_data.market_instrument import MarketInstrument
from src.market_data.market_quote_collection import MarketQuoteCollection
from src.pricing.dv01_calculator import DV01Calculator
from src.products.fixed_leg import FixedLeg
from src.products.floating_leg import FloatingLeg
from src.products.interest_rate_swap import InterestRateSwap
from src.products.trade import Trade


def test_dv01_calculator():

    quotes = MarketQuoteCollection()

    quotes.add(MarketInstrument("Deposit", "1M", 0.05))
    quotes.add(MarketInstrument("Deposit", "3M", 0.05))
    quotes.add(MarketInstrument("Deposit", "6M", 0.05))
    quotes.add(MarketInstrument("Deposit", "1Y", 0.05))
    quotes.add(MarketInstrument("Deposit", "2Y", 0.05))
    quotes.add(MarketInstrument("Deposit", "3Y", 0.05))

    curve = Bootstrapper(
        valuation_date=date(2026, 1, 1),
        market_quotes=quotes,
    ).build()

    trade = Trade(
        trade_id="IRS001",
        counterparty="ABC",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2029, 1, 1),
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
    )

    swap = InterestRateSwap(
        trade=trade,
        fixed_leg=fixed_leg,
        floating_leg=floating_leg,
    )

    result = DV01Calculator().calculate(
        swap,
        curve,
    )

    assert result.trade_id == "IRS001"
    assert result.currency == "USD"
    assert result.present_value > 0
    assert result.dv01 < 0