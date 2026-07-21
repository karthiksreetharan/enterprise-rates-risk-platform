from datetime import date

from pytest import raises

from src.schedule.payment_period import PaymentPeriod
from src.schedule.schedule import Schedule


def build_period(year: int) -> PaymentPeriod:

    return PaymentPeriod(
        accrual_start=date(year, 1, 1),
        accrual_end=date(year + 1, 1, 1),
        payment_date=date(year + 1, 1, 1),
    )


def test_schedule_creation():

    schedule = Schedule(
        periods=(
            build_period(2026),
            build_period(2027),
            build_period(2028),
        )
    )

    assert len(schedule) == 3


def test_start_date():

    schedule = Schedule(
        periods=(
            build_period(2026),
            build_period(2027),
        )
    )

    assert schedule.start_date == date(2026, 1, 1)


def test_end_date():

    schedule = Schedule(
        periods=(
            build_period(2026),
            build_period(2027),
        )
    )

    assert schedule.end_date == date(2028, 1, 1)


def test_first_period():

    schedule = Schedule(
        periods=(
            build_period(2026),
            build_period(2027),
        )
    )

    assert schedule.first_period.accrual_start == date(2026, 1, 1)


def test_last_period():

    schedule = Schedule(
        periods=(
            build_period(2026),
            build_period(2027),
        )
    )

    assert schedule.last_period.accrual_end == date(2028, 1, 1)


def test_empty_schedule():

    with raises(ValueError):

        Schedule(periods=())