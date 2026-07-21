"""
yield_curve.py

Represents a bootstrapped zero-coupon yield curve.
"""

from __future__ import annotations

from datetime import date
from math import exp

from src.curves.curve_point import CurvePoint
from src.curves.interpolation import linear_interpolate


class YieldCurve:
    """
    Zero-coupon yield curve supporting lookups by
    tenor, maturity, and payment date.
    """

    def __init__(
        self,
        valuation_date: date,
        curve_points: list[CurvePoint],
    ) -> None:

        if not curve_points:
            raise ValueError(
                "Yield curve must contain at least one curve point."
            )

        self.valuation_date = valuation_date

        self.curve_points = sorted(
            curve_points,
            key=lambda point: point.maturity,
        )

    # ---------------------------------------------------------
    # Private Utilities
    # ---------------------------------------------------------

    def _year_fraction(
        self,
        payment_date: date,
    ) -> float:
        """
        Convert a payment date into time to maturity.

        Stage 1 uses calendar years so that tenor-based
        curve pillars (1Y, 2Y, 3Y, ...) align exactly with
        payment dates, avoiding leap-year drift.
        """

        if payment_date < self.valuation_date:
            raise ValueError(
                "Payment date cannot be before valuation date."
            )

        years = payment_date.year - self.valuation_date.year
        months = payment_date.month - self.valuation_date.month
        days = payment_date.day - self.valuation_date.day

        return (
            years
            + months / 12.0
            + days / 365.0
        )

    # ---------------------------------------------------------
    # Lookup by Tenor
    # ---------------------------------------------------------

    def get_curve_point(
        self,
        tenor: str,
    ) -> CurvePoint:

        tenor = tenor.strip().upper()

        for point in self.curve_points:
            if point.tenor == tenor:
                return point

        raise ValueError(
            f"Unknown tenor '{tenor}'."
        )

    def get_zero_rate(
        self,
        tenor: str,
    ) -> float:

        return self.get_curve_point(
            tenor
        ).zero_rate

    def get_discount_factor(
        self,
        tenor: str,
    ) -> float:

        return self.get_curve_point(
            tenor
        ).discount_factor

    # ---------------------------------------------------------
    # Lookup by Maturity
    # ---------------------------------------------------------

    def get_zero_rate_by_time(
        self,
        maturity: float,
    ) -> float:

        first = self.curve_points[0]
        last = self.curve_points[-1]

        if maturity < first.maturity:
            raise ValueError(
                "Requested maturity is below curve range."
            )

        if maturity > last.maturity:
            raise ValueError(
                "Requested maturity is above curve range."
            )

        for point in self.curve_points:

            if abs(point.maturity - maturity) < 1e-12:
                return point.zero_rate

        for left, right in zip(
            self.curve_points[:-1],
            self.curve_points[1:],
        ):

            if left.maturity <= maturity <= right.maturity:

                return linear_interpolate(
                    maturity,
                    left.maturity,
                    left.zero_rate,
                    right.maturity,
                    right.zero_rate,
                )

        raise RuntimeError(
            "Interpolation failed."
        )

    def get_discount_factor_by_time(
        self,
        maturity: float,
    ) -> float:

        zero_rate = self.get_zero_rate_by_time(
            maturity
        )

        return exp(
            -zero_rate * maturity
        )

    # ---------------------------------------------------------
    # Lookup by Payment Date
    # ---------------------------------------------------------

    def zero_rate(
        self,
        payment_date: date,
    ) -> float:

        maturity = self._year_fraction(
            payment_date
        )

        return self.get_zero_rate_by_time(
            maturity
        )

    def discount_factor(
        self,
        payment_date: date,
    ) -> float:

        maturity = self._year_fraction(
            payment_date
        )

        return self.get_discount_factor_by_time(
            maturity
        )

    # ---------------------------------------------------------
    # Utilities
    # ---------------------------------------------------------

    def available_tenors(
        self,
    ) -> list[str]:

        return [
            point.tenor
            for point in self.curve_points
        ]

    def number_of_points(
        self,
    ) -> int:

        return len(
            self.curve_points
        )

    # ---------------------------------------------------------
    # Reporting
    # ---------------------------------------------------------

    def summary(
        self,
    ) -> None:

        print("=" * 72)
        print("Yield Curve")
        print("=" * 72)

        print(
            f"Valuation Date : {self.valuation_date}"
        )

        print()

        print(
            f"{'Tenor':<8}"
            f"{'Years':>10}"
            f"{'Zero Rate':>16}"
            f"{'Discount Factor':>22}"
        )

        print("-" * 72)

        for point in self.curve_points:

            print(
                f"{point.tenor:<8}"
                f"{point.maturity:>10.4f}"
                f"{point.zero_rate:>15.4%}"
                f"{point.discount_factor:>22.6f}"
            )

        print("-" * 72)
        print("Interpolation : Linear")
        print(
            f"Curve Points  : {self.number_of_points()}"
        )

    # ---------------------------------------------------------
    # Representation
    # ---------------------------------------------------------

    def __len__(
        self,
    ) -> int:

        return self.number_of_points()

    def __iter__(
        self,
    ):

        return iter(
            self.curve_points
        )

    def __repr__(
        self,
    ) -> str:

        return (
            "YieldCurve("
            f"valuation_date={self.valuation_date}, "
            f"points={len(self)})"
        )