"""
historical_var_engine.py

Engine for replaying historical market scenarios.
"""

from src.pricing.pricing_engine import PricingEngine
from src.risk.curve_shocker import CurveShocker
from src.risk.historical_scenario import HistoricalScenario
from src.risk.scenario_result import ScenarioResult


class HistoricalVaREngine:
    """
    Replays historical market scenarios and computes
    the resulting P&L distribution.
    """

    def __init__(self):

        self._pricing_engine = PricingEngine()
        self._curve_shocker = CurveShocker()

    def run(
        self,
        swap,
        curve,
        historical_scenarios: list[HistoricalScenario],
    ) -> list[ScenarioResult]:

        base_valuation = self._pricing_engine.value(
            swap,
            curve,
        )

        base_pv = base_valuation.present_value

        results = []

        for scenario in historical_scenarios:

            shocked_curve = self._curve_shocker.multi_bucket_shift(
                curve,
                scenario.tenor_shifts,
            )

            shocked_valuation = self._pricing_engine.value(
                swap,
                shocked_curve,
            )

            shocked_pv = shocked_valuation.present_value

            results.append(
                ScenarioResult(
                    scenario=str(scenario.scenario_date),
                    trade_id=swap.trade.trade_id,
                    currency=swap.trade.currency,
                    present_value=shocked_pv,
                    pnl=shocked_pv - base_pv,
                )
            )

        return results