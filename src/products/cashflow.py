from dataclasses import dataclass
from datetime import date


@dataclass
class Cashflow:
    """
    Represents a single contractual coupon period
    of an Interest Rate Swap.
    """

    trade_id: str
    period_number: int
    accrual_start: date
    accrual_end: date
    payment_date: date
    year_fraction: float
    leg_type: str

    def summary(self):
        """
        Displays the contractual information
        of the cashflow.
        """

        print("=" * 60)
        print(f"Trade ID      : {self.trade_id}")
        print(f"Coupon Period : {self.period_number}")
        print("=" * 60)
        print(f"Accrual Start : {self.accrual_start}")
        print(f"Accrual End   : {self.accrual_end}")
        print(f"Payment Date  : {self.payment_date}")
        print(f"Year Fraction : {self.year_fraction:.6f}")
        print(f"Leg Type      : {self.leg_type}")
        print("=" * 60)