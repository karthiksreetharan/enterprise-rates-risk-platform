"""
trade.py

Represents a generic financial trade.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class Trade:
    """
    Generic financial trade.

    Stores trade-level information that is common across
    all financial products.
    """

    trade_id: str
    counterparty: str
    currency: str
    effective_date: date
    maturity_date: date

    def __post_init__(self) -> None:

        if not self.trade_id.strip():
            raise ValueError(
                "Trade ID cannot be empty."
            )

        if not self.counterparty.strip():
            raise ValueError(
                "Counterparty cannot be empty."
            )

        if len(self.currency) != 3:
            raise ValueError(
                "Currency must be a 3-letter ISO code."
            )

        if self.effective_date >= self.maturity_date:
            raise ValueError(
                "Effective date must be before maturity date."
            )