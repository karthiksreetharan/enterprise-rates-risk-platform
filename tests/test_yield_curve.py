from datetime import date

from src.curves.bootstrapper import Bootstrapper
from src.market_data.market_instrument import MarketInstrument
from src.market_data.market_quote_collection import MarketQuoteCollection


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

    return Bootstrapper(
        date.today(),
        quotes,
    ).build()


def test_zero_rate():

    curve = build_curve()

    assert curve.get_zero_rate("6M") == 0.052


def test_discount_factor():

    curve = build_curve()

    assert curve.get_discount_factor("1Y") < 1


def test_interpolated_rate():

    curve = build_curve()

    rate = curve.get_zero_rate_by_time(0.75)

    assert 0.052 < rate < 0.055


def test_available_tenors():

    curve = build_curve()

    assert curve.available_tenors() == [
        "1M",
        "3M",
        "6M",
        "1Y",
    ]