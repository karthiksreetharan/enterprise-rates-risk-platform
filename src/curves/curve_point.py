"""
curve_point.py

Represents one point on a bootstrapped yield curve.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CurvePoint:
    """
    Immutable representation of a single point on the yield curve.

    Parameters
    ----------
    tenor : str
        Market tenor (e.g. "3M", "5Y").

    maturity : float
        Time to maturity in years.

    zero_rate : float
        Continuously compounded zero rate.

    discount_factor : float
        Discount factor corresponding to the maturity.
    """

    tenor: str
    maturity: float
    zero_rate: float
    discount_factor: float

    def __post_init__(self) -> None:

        if self.maturity <= 0:
            raise ValueError(
                "Maturity must be positive."
            )

        if not (0.0 < self.zero_rate < 1.0):
            raise ValueError(
                "Zero rate must be in decimal format between 0 and 1."
            )

        if not (0.0 < self.discount_factor <= 1.0):
            raise ValueError(
                "Discount factor must be between 0 and 1."
            )

    def __str__(self) -> str:
        return (
            f"{self.tenor:<6}"
            f"{self.maturity:>8.4f}Y"
            f"{self.zero_rate:>12.4%}"
            f"{self.discount_factor:>18.6f}"
        )