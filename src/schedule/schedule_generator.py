"""
schedule_generator.py

Generates payment schedules for Interest Rate Swaps.
"""

from __future__ import annotations

from dateutil.relativedelta import relativedelta

from src.products.interest_rate_swap import InterestRateSwap
from src.schedule.payment_period import PaymentPeriod
from src.schedule.schedule import Schedule


class ScheduleGenerator:
    """
    Generates payment schedules for an Interest Rate Swap.
    """

    def generate(
        self,
        swap: InterestRateSwap,
    ) -> Schedule:

        periods = []

        current_start = swap.trade.effective_date
        maturity = swap.trade.maturity_date

        frequency = swap.fixed_leg.payment_frequency

        # PaymentFrequency represents payments per year
        months = 12 // frequency.value

        while current_start < maturity:

            current_end = current_start + relativedelta(months=months)

            if current_end > maturity:
                current_end = maturity

            periods.append(
                PaymentPeriod(
                    accrual_start=current_start,
                    accrual_end=current_end,
                    payment_date=current_end,
                )
            )

            current_start = current_end

        return Schedule(tuple(periods))