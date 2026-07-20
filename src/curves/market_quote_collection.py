"""
market_quote_collection.py

Container for market instrument quotes used in yield curve construction.
"""

from __future__ import annotations

from src.common.constants import TENOR_TO_MONTHS
from src.curves.market_instrument import MarketInstrument


class MarketQuoteCollection:
    """
    Container for market instrument quotes.

    Responsible for:
    - Storing market quotes
    - Preventing duplicate tenors
    - Returning quotes sorted by maturity
    """

    def __init__(self) -> None:
        self._quotes: list[MarketInstrument] = []

    def add(self, quote: MarketInstrument) -> None:
        """
        Add a market instrument quote to the collection.
        """

        if not isinstance(quote, MarketInstrument):
            raise TypeError(
                "Only MarketInstrument objects can be added."
            )

        if any(existing.tenor == quote.tenor for existing in self._quotes):
            raise ValueError(
                f"Duplicate tenor found: {quote.tenor}"
            )

        self._quotes.append(quote)

    def get_all_quotes(self) -> list[MarketInstrument]:
        """
        Return all market quotes sorted by maturity.
        """

        return sorted(
            self._quotes,
            key=lambda quote: TENOR_TO_MONTHS[quote.tenor]
        )

    def is_empty(self) -> bool:
        """
        Check whether the collection is empty.
        """

        return len(self._quotes) == 0

    def summary(self) -> None:
        """
        Display all market quotes.
        """

        print("=" * 60)
        print("Market Quote Collection")
        print("=" * 60)

        print(
            f"{'Instrument':<15}"
            f"{'Tenor':<10}"
            f"{'Market Rate':>15}"
        )

        print("-" * 60)

        for quote in self.get_all_quotes():
            print(
                f"{quote.instrument_type:<15}"
                f"{quote.tenor:<10}"
                f"{quote.market_rate:>14.4%}"
            )

        print("-" * 60)
        print(f"Total Quotes : {len(self)}")

    def __len__(self) -> int:
        """
        Return the number of market quotes.
        """

        return len(self._quotes)

    def __iter__(self):
        """
        Iterate over market quotes sorted by maturity.
        """

        return iter(self.get_all_quotes())

    def __getitem__(self, index: int) -> MarketInstrument:
        """
        Access a market quote by index.
        """

        return self.get_all_quotes()[index]

    def __repr__(self) -> str:
        return (
            f"MarketQuoteCollection(size={len(self)})"
        )