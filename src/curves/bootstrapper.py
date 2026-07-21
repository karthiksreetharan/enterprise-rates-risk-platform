"""
bootstrapper.py

Constructs a YieldCurve from observable market quotes.
"""

from __future__ import annotations

from datetime import date
from math import exp

from src.common.constants import TENOR_TO_YEARS
from src.curves.curve_point import CurvePoint
from src.curves.yield_curve import YieldCurve
from src.market_data.market_quote_collection import MarketQuoteCollection


class Bootstrapper:
    """
    Builds a YieldCurve from market quotes.

    Stage 1 Assumptions
    -------------------
    - Market quotes are already zero rates.
    - Continuous compounding.
    """

    def __init__(
        self,
        valuation_date: date,
        market_quotes: MarketQuoteCollection,
    ) -> None:

        if market_quotes.is_empty():
            raise ValueError(
                "Market quote collection is empty."
            )

        self.valuation_date = valuation_date
        self.market_quotes = market_quotes

    def build(self) -> YieldCurve:
        """
        Build and return a YieldCurve.
        """

        curve_points: list[CurvePoint] = []

        for quote in self.market_quotes:

            maturity = TENOR_TO_YEARS[quote.tenor]

            zero_rate = quote.market_rate

            discount_factor = exp(
                -zero_rate * maturity
            )

            curve_points.append(
                CurvePoint(
                    tenor=quote.tenor,
                    maturity=maturity,
                    zero_rate=zero_rate,
                    discount_factor=discount_factor,
                )
            )

        return YieldCurve(
            valuation_date=self.valuation_date,
            curve_points=curve_points,
        )