"""
Scenario analysis engine.
"""

from src.pricing.pricing_engine import PricingEngine
from src.risk.curve_shocker import CurveShocker
from src.risk.scenario import Scenario
from src.risk.scenario_result import ScenarioResult


class ScenarioEngine:

    def __init__(self):

        self._pricing_engine = PricingEngine()
        self._curve_shocker = CurveShocker()

    def run(
        self,
        swap,
        curve,
        scenario: Scenario,
    ) -> ScenarioResult:

        base = self._pricing_engine.value(
            swap,
            curve,
        )

        shocked_curve = self._curve_shocker.parallel_shift(
            curve,
            scenario.parallel_shift,
        )

        stressed = self._pricing_engine.value(
            swap,
            shocked_curve,
        )

        return ScenarioResult(
            scenario=scenario.name,
            trade_id=base.trade_id,
            currency=base.currency,
            present_value=stressed.present_value,
            pnl=stressed.present_value - base.present_value,
        )