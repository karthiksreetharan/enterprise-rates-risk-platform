"""
historical_var_report_engine.py

Computes summary statistics from a historical
P&L distribution.

The report includes:

- Number of scenarios
- Best gain
- Worst loss
- Mean P&L
- Median P&L
- Historical VaR (95%)
- Historical VaR (99%)
"""

from math import ceil
from statistics import mean, median

from src.risk.historical_var_report import HistoricalVaRReport


class HistoricalVaRReportEngine:
    """
    Computes summary statistics from a historical
    P&L distribution.
    """

    def run(
        self,
        scenario_results,
    ) -> HistoricalVaRReport:
        """
        Build a Historical VaR report from a collection
        of scenario results.

        Parameters
        ----------
        scenario_results
            Collection of ScenarioResult objects.

        Returns
        -------
        HistoricalVaRReport
        """

        if not scenario_results:
            raise ValueError(
                "scenario_results cannot be empty."
            )

        pnls = sorted(
            [result.pnl for result in scenario_results]
        )

        number_of_scenarios = len(pnls)

        var95_index = max(
            0,
            ceil(0.05 * number_of_scenarios) - 1,
        )

        var99_index = max(
            0,
            ceil(0.01 * number_of_scenarios) - 1,
        )

        return HistoricalVaRReport(

            number_of_scenarios=number_of_scenarios,

            best_gain=max(pnls),

            worst_loss=min(pnls),

            average_pnl=mean(pnls),

            median_pnl=median(pnls),

            var_95=abs(pnls[var95_index]),

            var_99=abs(pnls[var99_index]),
        )