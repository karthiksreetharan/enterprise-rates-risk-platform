"""
interpolation.py

Interpolation utilities for yield curves.
"""

from __future__ import annotations


def linear_interpolate(
    x: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    allow_extrapolation: bool = False,
) -> float:
    """
    Perform linear interpolation.

    Parameters
    ----------
    x
        Target x-coordinate.

    x1, y1
        First known point.

    x2, y2
        Second known point.

    allow_extrapolation
        Allow interpolation outside [x1, x2].

    Returns
    -------
    float
        Interpolated value.
    """

    if x2 <= x1:
        raise ValueError(
            "x2 must be greater than x1."
        )

    if (
        not allow_extrapolation
        and not (x1 <= x <= x2)
    ):
        raise ValueError(
            "Interpolation point lies outside interval."
        )

    weight = (x - x1) / (x2 - x1)

    return y1 + weight * (y2 - y1)