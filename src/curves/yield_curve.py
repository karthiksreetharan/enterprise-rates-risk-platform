"""
yield_curve.py

Represents a bootstrapped yield curve.
"""

from __future__ import annotations

from datetime import date


class YieldCurve:
    """
    Represents a completed yield curve.

    Stores zero rates and discount factors
    for each market tenor.
    """

    def __init__(
        self,
        valuation_date: date,
        zero_rates: dict[str, float],
        discount_factors: dict[str, float],
    ) -> None:

        self.valuation_date = valuation_date
        self.zero_rates = zero_rates
        self.discount_factors = discount_factors

    def get_zero_rate(self, tenor: str) -> float:
        """
        Return the zero rate for a tenor.
        """

        return self.zero_rates[tenor]

    def get_discount_factor(self, tenor: str) -> float:
        """
        Return the discount factor for a tenor.
        """

        return self.discount_factors[tenor]

    def summary(self) -> None:
        """
        Display the yield curve.
        """

        print("=" * 70)
        print("Yield Curve")
        print("=" * 70)

        print(f"Valuation Date : {self.valuation_date}")
        print()

        print(
            f"{'Tenor':<10}"
            f"{'Zero Rate':>15}"
            f"{'Discount Factor':>22}"
        )

        print("-" * 70)

        for tenor in self.zero_rates:

            print(
                f"{tenor:<10}"
                f"{self.zero_rates[tenor]:>14.4%}"
                f"{self.discount_factors[tenor]:>21.6f}"
            )

        print("-" * 70)

    def __repr__(self) -> str:

        return (
            f"YieldCurve("
            f"valuation_date={self.valuation_date}, "
            f"points={len(self.zero_rates)})"
        )