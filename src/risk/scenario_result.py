"""
Scenario analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ScenarioResult:

    scenario: str

    trade_id: str

    currency: str

    present_value: float

    pnl: float