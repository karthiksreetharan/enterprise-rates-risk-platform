from dateutil.relativedelta import relativedelta
from src.products.cashflow import Cashflow
from src.products.interest_rate_swap import InterestRateSwap


class ScheduleGenerator:
    """
    Generates contractual cashflow schedules
    for an Interest Rate Swap.
    """

    def __init__(self):
        pass

    def _frequency_to_months(self, frequency: str) -> int:
        """
        Converts payment frequency into
        the corresponding number of months.
        """

        frequency_mapping = {
            "Monthly": 1,
            "Quarterly": 3,
            "Semi-Annual": 6,
            "Annual": 12
        }

        if frequency not in frequency_mapping:
            raise ValueError(
                f"Unsupported payment frequency: {frequency}"
            )

        return frequency_mapping[frequency]

    def generate(self, swap: InterestRateSwap) -> list[Cashflow]:
        """
        Generates the contractual cashflow schedule
        for an Interest Rate Swap.
        """

        cashflows = []

        months = self._frequency_to_months(
            swap.payment_frequency
        )

        current_date = swap.effective_date

        period = 1

        while current_date < swap.maturity_date:

            next_date = current_date + relativedelta(
                months=months
            )

            cashflow = Cashflow(
                trade_id=swap.trade_id,
                period_number=period,
                accrual_start=current_date,
                accrual_end=next_date,
                payment_date=next_date,
                year_fraction=months / 12,
                leg_type="Fixed"
            )

            cashflows.append(cashflow)

            current_date = next_date

            period += 1

        return cashflows