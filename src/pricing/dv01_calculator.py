"""
dv01_calculator.py

Computes DV01 using finite-difference repricing.
"""

from __future__ import annotations

from src.pricing.pricing_engine import PricingEngine
from src.products.dv01_result import DV01Result
from src.products.interest_rate_swap import InterestRateSwap
from src.curves.yield_curve import YieldCurve
from src.risk.curve_shocker import CurveShocker


class DV01Calculator:
    """
    Computes DV01 by applying a parallel 1 bp shift
    to the yield curve and repricing the swap.
    """

    BUMP_SIZE = 0.0001  # 1 basis point

    def calculate(
        self,
        swap: InterestRateSwap,
        curve: YieldCurve,
    ) -> DV01Result:
        """
        Calculate the DV01 of an interest rate swap.

        Parameters
        ----------
        swap
            Interest rate swap.

        curve
            Base yield curve.

        Returns
        -------
        DV01Result
        """

        pricing_engine = PricingEngine()

        # Base valuation
        base = pricing_engine.value(
            swap,
            curve,
        )

        # Parallel +1 bp shift
        shifted_curve = CurveShocker().parallel_shift(
            curve,
            self.BUMP_SIZE,
        )

        # Reprice on shifted curve
        bumped = pricing_engine.value(
            swap,
            shifted_curve,
        )

        return DV01Result(
            trade_id=base.trade_id,
            currency=base.currency,
            present_value=base.present_value,
            dv01=bumped.present_value - base.present_value,
        )