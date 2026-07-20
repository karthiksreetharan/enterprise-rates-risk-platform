from dataclasses import dataclass
from datetime import date


@dataclass
class InterestRateSwap:
    """
    Represents the contractual terms of a vanilla
    fixed-for-floating Interest Rate Swap.
    """

    trade_id: str
    counterparty: str
    currency: str
    notional: float
    fixed_rate: float
    floating_index: str
    pay_fixed: bool
    effective_date: date
    maturity_date: date
    payment_frequency: str
    day_count_convention: str
    status: str

    def __post_init__(self):
        """
        Performs business validation immediately
        after object creation.
        """
        self._validate()

    def _validate(self):
        """
        Validates the contractual attributes of
        the Interest Rate Swap.
        """

        if self.notional <= 0:
            raise ValueError(
                "Notional amount must be positive."
            )

        if not 0 <= self.fixed_rate <= 1:
            raise ValueError(
                "Fixed rate must be expressed as a decimal between 0 and 1."
            )

        if self.effective_date >= self.maturity_date:
            raise ValueError(
                "Maturity date must be later than the effective date."
            )

        valid_frequencies = {
            "Monthly",
            "Quarterly",
            "Semi-Annual",
            "Annual"
        }

        if self.payment_frequency not in valid_frequencies:
            raise ValueError(
                f"Unsupported payment frequency: {self.payment_frequency}"
            )

        valid_day_count_conventions = {
            "ACT/360",
            "ACT/365",
            "30/360"
        }

        if self.day_count_convention not in valid_day_count_conventions:
            raise ValueError(
                f"Unsupported day count convention: {self.day_count_convention}"
            )

    def summary(self):
        """
        Displays a formatted summary of the trade.
        """

        direction = (
            "Pay Fixed"
            if self.pay_fixed
            else "Receive Fixed"
        )

        print("=" * 60)
        print("INTEREST RATE SWAP")
        print("=" * 60)
        print(f"Trade ID            : {self.trade_id}")
        print(f"Counterparty        : {self.counterparty}")
        print(f"Currency            : {self.currency}")
        print(f"Notional            : {self.notional:,.0f}")
        print(f"Direction           : {direction}")
        print(f"Fixed Rate          : {self.fixed_rate:.4%}")
        print(f"Floating Index      : {self.floating_index}")
        print(f"Effective Date      : {self.effective_date}")
        print(f"Maturity Date       : {self.maturity_date}")
        print(f"Payment Frequency   : {self.payment_frequency}")
        print(f"Day Count           : {self.day_count_convention}")
        print(f"Status              : {self.status}")
        print("=" * 60)