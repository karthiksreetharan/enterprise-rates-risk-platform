"""
swap_pricer.py

Values an interest rate swap by aggregating
discounted cash flows.
"""

from __future__ import annotations

from src.products.discounted_cashflow import DiscountedCashFlow
from src.products.interest_rate_swap import InterestRateSwap
from src.products.swap_valuation import SwapValuation


class SwapPricer:
    """
    Computes the present value of an interest rate swap.

    Stage 1
    -------
    Only fixed-leg cash flows are available.

    PV = Sum(Discounted Cash Flows)
    """

    def value(
        self,
        swap: InterestRateSwap,
        discounted_cashflows: tuple[DiscountedCashFlow, ...],
    ) -> SwapValuation:

        pv = sum(
            cf.present_value
            for cf in discounted_cashflows
        )

        return SwapValuation(
            trade_id=swap.trade.trade_id,
            currency=swap.trade.currency,
            present_value=pv,
        )