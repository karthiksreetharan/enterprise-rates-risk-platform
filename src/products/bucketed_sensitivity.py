"""
bucketed_sensitivity.py

Represents the sensitivity of a trade to a single curve tenor.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BucketedSensitivity:
    """
    Sensitivity for a single tenor.
    """

    tenor: str
    sensitivity: float