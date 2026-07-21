"""
bucketed_dv01_result.py

Container for bucketed DV01 results.
"""

from dataclasses import dataclass

from src.products.bucketed_sensitivity import BucketedSensitivity


@dataclass(frozen=True, slots=True)
class BucketedDV01Result:
    """
    Bucketed DV01 output.
    """

    trade_id: str
    currency: str
    present_value: float
    bucketed_dv01: tuple[BucketedSensitivity, ...]