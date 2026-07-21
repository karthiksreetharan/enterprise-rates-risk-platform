"""
schedule.py

Represents the payment schedule of an Interest Rate Swap.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.schedule.payment_period import PaymentPeriod


@dataclass(frozen=True, slots=True)
class Schedule:
    """
    Collection of payment periods.
    """

    periods: tuple[PaymentPeriod, ...]

    def __post_init__(self) -> None:

        if len(self.periods) == 0:
            raise ValueError(
                "Schedule must contain at least one payment period."
            )

    def __len__(self) -> int:
        return len(self.periods)

    def __iter__(self):
        return iter(self.periods)

    def __getitem__(self, index: int) -> PaymentPeriod:
        return self.periods[index]

    @property
    def start_date(self):
        return self.periods[0].accrual_start

    @property
    def end_date(self):
        return self.periods[-1].accrual_end

    @property
    def first_period(self) -> PaymentPeriod:
        return self.periods[0]

    @property
    def last_period(self) -> PaymentPeriod:
        return self.periods[-1]