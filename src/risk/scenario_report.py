from dataclasses import dataclass

from src.risk.scenario_result import ScenarioResult


@dataclass(frozen=True, slots=True)
class ScenarioReport:

    results: list[ScenarioResult]