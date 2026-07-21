"""
floating_leg.py

Represents the floating leg of an Interest Rate Swap.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.common.enums import FloatingIndex
from src.products.leg import Leg


@dataclass(frozen=True, slots=True)
class FloatingLeg(Leg):
    """
    Floating-rate leg.
    """

    floating_index: FloatingIndex
    spread: float = 0.0

    def __post_init__(self) -> None:

        self._validate()

        if not isinstance(self.spread, (int, float)):
            raise TypeError("Spread must be numeric.")

        # Allow negative spreads in practice.