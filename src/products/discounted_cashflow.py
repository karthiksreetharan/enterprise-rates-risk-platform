"""
discounted_cashflow.py

Represents the present value of a contractual cash flow.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.products.cashflow import CashFlow


@dataclass(frozen=True, slots=True)
class DiscountedCashFlow:
    """
    Immutable representation of a discounted cash flow.

    Parameters
    ----------
    cashflow : CashFlow
        Original contractual cash flow.

    discount_factor : float
        Discount factor used for valuation.

    present_value : float
        Present value of the cash flow.
    """

    cashflow: CashFlow
    discount_factor: float
    present_value: float

    def __post_init__(self) -> None:

        if not (0.0 < self.discount_factor <= 1.0):
            raise ValueError(
                "Discount factor must be between 0 and 1."
            )

    @property
    def payment_date(self):
        return self.cashflow.payment_date

    @property
    def amount(self):
        return self.cashflow.amount

    @property
    def currency(self):
        return self.cashflow.currency

    @property
    def cashflow_type(self):
        return self.cashflow.cashflow_type

    def __str__(self) -> str:

        return (
            f"{self.payment_date}"
            f" | DF={self.discount_factor:.6f}"
            f" | CF={self.amount:,.2f}"
            f" | PV={self.present_value:,.2f}"
        )