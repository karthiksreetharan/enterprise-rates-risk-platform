"""
curve_builder.py

Constructs a yield curve from market quotes.
"""

from __future__ import annotations

from datetime import date

from src.curves.market_quote_collection import MarketQuoteCollection
from src.curves.yield_curve import YieldCurve


class CurveBuilder:
    """
    Builds a yield curve from market quotes.
    """

    def __init__(self) -> None:
        pass

    def build(
        self,
        valuation_date: date,
        market_quotes: MarketQuoteCollection,
    ) -> YieldCurve:
        """
        Build a yield curve.
        """

        if market_quotes.is_empty():
            raise ValueError("Market quote collection is empty.")

        zero_rates = {}
        discount_factors = {}

        return YieldCurve(
            valuation_date=valuation_date,
            zero_rates=zero_rates,
            discount_factors=discount_factors,
        )

    def __repr__(self) -> str:
        return "CurveBuilder()"