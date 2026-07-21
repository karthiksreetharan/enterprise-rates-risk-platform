from datetime import date

from src.curves.bootstrapper import Bootstrapper
from src.market_data.market_instrument import MarketInstrument
from src.market_data.market_quote_collection import MarketQuoteCollection
from src.risk.curve_shocker import CurveShocker


def test_parallel_shift():

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

    shocked = CurveShocker().parallel_shift(
        curve,
        0.0001,
    )

    for original, shifted in zip(curve, shocked):

        assert shifted.zero_rate == original.zero_rate + 0.0001