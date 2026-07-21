"""
pricing_engine.py

High-level pricing engine for interest rate swaps.
"""

from __future__ import annotations

from src.cashflows.cashflow_generator import CashFlowGenerator
from src.curves.yield_curve import YieldCurve
from src.pricing.discounting import Discounting
from src.pricing.swap_pricer import SwapPricer
from src.products.interest_rate_swap import InterestRateSwap
from src.products.swap_valuation import SwapValuation
from src.schedule.schedule_generator import ScheduleGenerator


class PricingEngine:
    """
    High-level pricing engine.

    Workflow
    --------
    InterestRateSwap
        ↓
    Schedule Generation
        ↓
    Cash Flow Generation
        ↓
    Discounting
        ↓
    Swap Pricing
        ↓
    Swap Valuation
    """

    def value(
        self,
        swap: InterestRateSwap,
        curve: YieldCurve,
    ) -> SwapValuation:

        schedule = ScheduleGenerator().generate(
            swap
        )

        cashflows = CashFlowGenerator().generate(
            swap,
            schedule,
        )

        discounted_cashflows = Discounting().discount(
            cashflows,
            curve,
        )

        return SwapPricer().value(
            swap,
            discounted_cashflows,
        )