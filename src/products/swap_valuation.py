"""
swap_valuation.py

Represents the valuation result of an interest rate swap.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SwapValuation:
    """
    Result of valuing an interest rate swap.
    """

    trade_id: str
    currency: str
    present_value: float

    def __repr__(self) -> str:

        return (
            "SwapValuation("
            f"trade_id='{self.trade_id}', "
            f"currency='{self.currency}', "
            f"present_value={self.present_value:,.2f})"
        )