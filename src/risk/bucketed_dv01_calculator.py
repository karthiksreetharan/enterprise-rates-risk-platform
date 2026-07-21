"""
bucketed_dv01_calculator.py

Computes key-rate (bucketed) DV01.
"""

from __future__ import annotations

from src.pricing.pricing_engine import PricingEngine
from src.products.bucketed_dv01_result import BucketedDV01Result
from src.products.bucketed_sensitivity import BucketedSensitivity
from src.products.interest_rate_swap import InterestRateSwap
from src.curves.yield_curve import YieldCurve
from src.risk.curve_shocker import CurveShocker


class BucketedDV01Calculator:

    BUMP_SIZE = 0.0001

    def __init__(self) -> None:
        self._pricing_engine = PricingEngine()
        self._curve_shocker = CurveShocker()

    def calculate(
        self,
        swap: InterestRateSwap,
        curve: YieldCurve,
    ) -> BucketedDV01Result:

        base = self._pricing_engine.value(
            swap,
            curve,
        )

        sensitivities: list[BucketedSensitivity] = []

        for point in curve:

            shocked_curve = self._curve_shocker.bucket_shift(
                curve,
                tenor=point.tenor,
                shift=self.BUMP_SIZE,
            )

            bumped = self._pricing_engine.value(
                swap,
                shocked_curve,
            )

            sensitivities.append(
                BucketedSensitivity(
                    tenor=point.tenor,
                    sensitivity=bumped.present_value - base.present_value,
                )
            )

        return BucketedDV01Result(
            trade_id=base.trade_id,
            currency=base.currency,
            present_value=base.present_value,
            bucketed_dv01=tuple(sensitivities),
        )