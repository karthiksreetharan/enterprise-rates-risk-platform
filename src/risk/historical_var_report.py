"""
historical_var_report.py

Summary statistics for Historical VaR.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HistoricalVaRReport:

    number_of_scenarios: int

    best_gain: float

    worst_loss: float

    average_pnl: float

    median_pnl: float

    var_95: float

    var_99: float