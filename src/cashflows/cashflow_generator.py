"""
cashflow_generator.py

Generates contractual cash flows for a vanilla
Interest Rate Swap.
"""

from __future__ import annotations

from src.common.enums import CashFlowType
from src.products.cashflow import CashFlow
from src.products.interest_rate_swap import InterestRateSwap
from src.schedule.schedule import Schedule


class CashFlowGenerator:
    """Generates fixed-leg cash flows."""

    def generate(
        self,
        swap: InterestRateSwap,
        schedule: Schedule,
    ) -> tuple[CashFlow, ...]:

        cashflows = []

        for period in schedule:

            year_fraction = period.accrual_days / 365.0

            amount = (
                swap.fixed_leg.notional
                * swap.fixed_leg.fixed_rate
                * year_fraction
            )

            cashflows.append(
                CashFlow(
                    payment_date=period.payment_date,
                    accrual_start=period.accrual_start,
                    accrual_end=period.accrual_end,
                    year_fraction=year_fraction,
                    notional=swap.fixed_leg.notional,
                    rate=swap.fixed_leg.fixed_rate,
                    amount=amount,
                    currency=swap.trade.currency,
                    cashflow_type=CashFlowType.FIXED,
                )
            )

        return tuple(cashflows)