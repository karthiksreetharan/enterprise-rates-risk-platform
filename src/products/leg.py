"""
leg.py

Base class for all swap legs.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.common.enums import (
    DayCountConvention,
    PaymentFrequency,
    PayReceive,
)


@dataclass(frozen=True, slots=True)
class Leg:
    """
    Base class representing a swap leg.
    """

    notional: float
    payment_frequency: PaymentFrequency
    day_count: DayCountConvention
    pay_receive: PayReceive

    def _validate(self) -> None:
        """Shared validation for all swap legs."""

        if not isinstance(self.notional, (int, float)):
            raise TypeError("Notional must be numeric.")

        if self.notional <= 0:
            raise ValueError("Notional must be positive.")

    @property
    def is_pay(self) -> bool:
        return self.pay_receive == PayReceive.PAY

    @property
    def is_receive(self) -> bool:
        return self.pay_receive == PayReceive.RECEIVE