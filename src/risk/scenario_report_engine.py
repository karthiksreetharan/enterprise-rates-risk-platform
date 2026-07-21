"""
Scenario report engine.
"""

from src.risk.scenario import Scenario
from src.risk.scenario_engine import ScenarioEngine
from src.risk.scenario_report import ScenarioReport


class ScenarioReportEngine:
    """
    Runs multiple scenarios and returns a scenario report.
    """

    def __init__(self):

        self._engine = ScenarioEngine()

    def run(
        self,
        swap,
        curve,
        scenarios: list[Scenario],
    ) -> ScenarioReport:

        results = []

        for scenario in scenarios:

            results.append(
                self._engine.run(
                    swap,
                    curve,
                    scenario,
                )
            )

        return ScenarioReport(results=results)