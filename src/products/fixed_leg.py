"""
fixed_leg.py

Represents the fixed leg of an Interest Rate Swap.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.products.leg import Leg


@dataclass(frozen=True, slots=True)
class FixedLeg(Leg):
    """
    Fixed-rate leg.
    """

    fixed_rate: float

    def __post_init__(self) -> None:

        self._validate()

        if not isinstance(self.fixed_rate, (int, float)):
            raise TypeError("Fixed rate must be numeric.")

        if self.fixed_rate < 0:
            raise ValueError("Fixed rate cannot be negative.")