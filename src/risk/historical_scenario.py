"""
Historical market scenario.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class HistoricalScenario:
    """
    Represents one historical market scenario.
    """

    scenario_date: date

    tenor_shifts: dict[str, float]