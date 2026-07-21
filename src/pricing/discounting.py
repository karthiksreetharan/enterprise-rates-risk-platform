"""
discounting.py

Discounts contractual cash flows using a yield curve.
"""

from __future__ import annotations

from src.curves.yield_curve import YieldCurve
from src.products.cashflow import CashFlow
from src.products.discounted_cashflow import DiscountedCashFlow


class Discounting:
    """
    Discount contractual cash flows to present value.
    """

    def discount(
        self,
        cashflows: tuple[CashFlow, ...],
        curve: YieldCurve,
    ) -> tuple[DiscountedCashFlow, ...]:
        """
        Discount every contractual cash flow.

        Parameters
        ----------
        cashflows : tuple[CashFlow, ...]
            Contractual cash flows.

        curve : YieldCurve
            Yield curve used for discounting.

        Returns
        -------
        tuple[DiscountedCashFlow, ...]
        """

        discounted = []

        for cashflow in cashflows:

            df = curve.discount_factor(
                cashflow.payment_date
            )

            pv = cashflow.amount * df

            discounted.append(
                DiscountedCashFlow(
                    cashflow=cashflow,
                    discount_factor=df,
                    present_value=pv,
                )
            )

        return tuple(discounted)