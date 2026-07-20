"""
market_instrument.py

Defines a single observable market quote used for yield curve construction.
"""

from __future__ import annotations

from src.common.constants import (
    SUPPORTED_INSTRUMENTS,
    SUPPORTED_TENORS,
)


class MarketInstrument:
    """
    Represents a single observable market quote.

    Example
    -------
    Deposit 3M @ 5.10%
    Swap 5Y @ 5.65%
    """

    def __init__(
        self,
        instrument_type: str,
        tenor: str,
        market_rate: float,
    ) ->None:
        self.instrument_type = instrument_type.strip().title()
        self.tenor = tenor.strip().upper()
        self.market_rate = float(market_rate)

        self._validate()

    def _validate(self) -> None:
        """
        Validate market instrument attributes.
        """

        if self.instrument_type not in SUPPORTED_INSTRUMENTS:
            raise ValueError(
                f"Unsupported instrument type: '{self.instrument_type}'. "
                f"Supported instruments: {sorted(SUPPORTED_INSTRUMENTS)}"
            )

        if self.tenor not in SUPPORTED_TENORS:
            raise ValueError(
                f"Unsupported tenor: '{self.tenor}'. "
                f"Supported tenors: {sorted(SUPPORTED_TENORS)}"
            )

        if not (0.0 < self.market_rate < 1.0):
            raise ValueError(
                "Market rate must be between 0 and 1 (decimal format). "
                "Example: 5% should be entered as 0.05."
            )

    def summary(self) -> None:
        """
        Display market instrument details.
        """

        print("=" * 40)
        print("Market Instrument")
        print("=" * 40)
        print(f"Instrument Type : {self.instrument_type}")
        print(f"Tenor           : {self.tenor}")
        print(f"Market Rate     : {self.market_rate:.4%}")

    def __repr__(self) -> str:
        return (
            f"MarketInstrument("
            f"instrument_type='{self.instrument_type}', "
            f"tenor='{self.tenor}', "
            f"market_rate={self.market_rate:.6f})"
        )