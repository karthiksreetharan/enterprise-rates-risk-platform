"""
dv01_calculator.py

Computes DV01 using finite-difference repricing.
"""

from __future__ import annotations

from math import exp

from src.curves.curve_point import CurvePoint
from src.curves.yield_curve import YieldCurve
from src.pricing.pricing_engine import PricingEngine
from src.products.dv01_result import DV01Result
from src.products.interest_rate_swap import InterestRateSwap


class DV01Calculator:
    """
    Computes DV01 by bumping the yield curve
    by one basis point (1 bp).
    """

    BUMP_SIZE = 0.0001

    def calculate(
        self,
        swap: InterestRateSwap,
        curve: YieldCurve,
    ) -> DV01Result:

        base = PricingEngine().value(
            swap,
            curve,
        )

        shifted_points = []

        for point in curve:

            bumped_rate = (
                point.zero_rate + self.BUMP_SIZE
            )

            shifted_points.append(
                CurvePoint(
                    tenor=point.tenor,
                    maturity=point.maturity,
                    zero_rate=bumped_rate,
                    discount_factor=exp(
                        -bumped_rate * point.maturity
                    ),
                )
            )

        shifted_curve = YieldCurve(
            valuation_date=curve.valuation_date,
            curve_points=shifted_points,
        )

        bumped = PricingEngine().value(
            swap,
            shifted_curve,
        )

        return DV01Result(
            trade_id=base.trade_id,
            currency=base.currency,
            present_value=base.present_value,
            dv01=bumped.present_value - base.present_value,
        )