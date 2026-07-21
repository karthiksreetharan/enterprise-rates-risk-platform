"""
interest_rate_swap.py

Represents a vanilla Interest Rate Swap.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.products.fixed_leg import FixedLeg
from src.products.floating_leg import FloatingLeg
from src.products.trade import Trade


@dataclass(frozen=True, slots=True)
class InterestRateSwap:
    """
    Vanilla Interest Rate Swap.
    """

    trade: Trade
    fixed_leg: FixedLeg
    floating_leg: FloatingLeg

    def __post_init__(self) -> None:

        if self.fixed_leg.notional != self.floating_leg.notional:
            raise ValueError(
                "Fixed and floating notionals must match."
            )

        if (
            self.fixed_leg.payment_frequency
            != self.floating_leg.payment_frequency
        ):
            raise ValueError(
                "Payment frequencies must match."
            )

        if (
            self.fixed_leg.pay_receive
            == self.floating_leg.pay_receive
        ):
            raise ValueError(
                "One leg must pay and the other must receive."
            )