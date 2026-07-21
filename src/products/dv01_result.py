"""
dv01_result.py

Represents the DV01 risk measure of an interest rate swap.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DV01Result:
    """
    Result of a DV01 calculation.
    """

    trade_id: str
    currency: str
    present_value: float
    dv01: float

    def __repr__(self) -> str:

        return (
            "DV01Result("
            f"trade_id='{self.trade_id}', "
            f"currency='{self.currency}', "
            f"present_value={self.present_value:,.2f}, "
            f"dv01={self.dv01:,.2f})"
        )