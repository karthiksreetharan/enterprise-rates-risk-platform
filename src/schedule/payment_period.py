"""
payment_period.py

Represents a single coupon period for an Interest Rate Swap.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class PaymentPeriod:
    """
    Represents one accrual period of a swap.

    Example
    -------
    Accrual Start : 01-Jan-2026
    Accrual End   : 01-Jan-2027
    Payment Date  : 01-Jan-2027
    """

    accrual_start: date
    accrual_end: date
    payment_date: date

    def __post_init__(self) -> None:

        if self.accrual_start >= self.accrual_end:
            raise ValueError(
                "Accrual start must be before accrual end."
            )

        if self.payment_date < self.accrual_end:
            raise ValueError(
                "Payment date cannot be before accrual end."
            )

    @property
    def accrual_days(self) -> int:
        """
        Number of calendar days in the accrual period.
        """

        return (self.accrual_end - self.accrual_start).days