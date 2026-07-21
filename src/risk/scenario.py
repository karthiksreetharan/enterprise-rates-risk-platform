"""
Scenario definition.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Scenario:
    """
    Represents a market scenario.
    """

    name: str
    parallel_shift: float = 0.0