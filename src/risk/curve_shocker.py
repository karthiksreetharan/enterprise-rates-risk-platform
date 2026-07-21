"""
curve_shocker.py

Reusable utilities for applying shocks to a yield curve.
"""

from __future__ import annotations

from math import exp

from src.curves.curve_point import CurvePoint
from src.curves.yield_curve import YieldCurve


class CurveShocker:
    """
    Utility class for generating shocked yield curves.

    All methods return NEW YieldCurve instances.
    The original curve is never modified.
    """

    def parallel_shift(
        self,
        curve: YieldCurve,
        shift: float,
    ) -> YieldCurve:
        """
        Apply a parallel shift to every zero rate.

        Parameters
        ----------
        curve
            Original yield curve.

        shift
            Shift in decimal.
            Example:
                +0.0001 = +1 bp
                -0.0001 = -1 bp
        """

        shocked_points = []

        for point in curve:

            new_rate = point.zero_rate + shift

            shocked_points.append(
                CurvePoint(
                    tenor=point.tenor,
                    maturity=point.maturity,
                    zero_rate=new_rate,
                    discount_factor=exp(
                        -new_rate * point.maturity
                    ),
                )
            )

        return YieldCurve(
            valuation_date=curve.valuation_date,
            curve_points=shocked_points,
        )