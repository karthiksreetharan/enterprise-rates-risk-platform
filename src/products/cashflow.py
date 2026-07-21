"""
cashflow.py

Represents a single contractual cash flow generated from an
Interest Rate Swap leg.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.common.enums import CashFlowType


@dataclass(frozen=True, slots=True)
class CashFlow:
    """
    Represents a single contractual coupon cash flow.

    A cash flow is generated from one payment period of an
    Interest Rate Swap leg and contains all information
    required for pricing, discounting, and risk analytics.
    """

    payment_date: date

    accrual_start: date
    accrual_end: date

    year_fraction: float

    notional: float
    rate: float
    amount: float

    currency: str
    cashflow_type: CashFlowType

    def __post_init__(self) -> None:
        """Validate cash flow attributes."""

        if self.accrual_start >= self.accrual_end:
            raise ValueError(
                "Accrual start must be before accrual end."
            )

        if self.year_fraction <= 0:
            raise ValueError(
                "Year fraction must be positive."
            )

        if self.notional <= 0:
            raise ValueError(
                "Notional must be positive."
            )

        if not self.currency:
            raise ValueError(
                "Currency cannot be empty."
            )