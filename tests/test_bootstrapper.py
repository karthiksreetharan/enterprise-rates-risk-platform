from datetime import date

from src.curves.bootstrapper import Bootstrapper
from src.market_data.market_instrument import MarketInstrument
from src.market_data.market_quote_collection import MarketQuoteCollection


def test_build_curve():

    quotes = MarketQuoteCollection()

    quotes.add(
        MarketInstrument("Deposit", "1M", 0.048)
    )

    quotes.add(
        MarketInstrument("Deposit", "3M", 0.050)
    )

    builder = Bootstrapper(
        valuation_date=date.today(),
        market_quotes=quotes,
    )

    curve = builder.build()

    assert len(curve) == 2


def test_empty_collection():

    quotes = MarketQuoteCollection()

    try:
        Bootstrapper(
            valuation_date=date.today(),
            market_quotes=quotes,
        )

        assert False

    except ValueError:

        assert True