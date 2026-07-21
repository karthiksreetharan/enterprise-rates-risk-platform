"""
cashflow.py

Represents a single cashflow generated from an IRS leg.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class Cashflow:
    """
    Represents a single payment.
    """

    payment_date: date
    accrual_start: date
    accrual_end: date

    year_fraction: float

    amount: float

    def __post_init__(self) -> None:

        if self.accrual_start >= self.accrual_end:
            raise ValueError(
                "Accrual start must be before accrual end."
            )

        if self.year_fraction <= 0:
            raise ValueError(
                "Year fraction must be positive."
            )