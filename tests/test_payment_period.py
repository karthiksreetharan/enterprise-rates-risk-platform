from datetime import date

from pytest import raises

from src.schedule.payment_period import PaymentPeriod


def test_payment_period_creation():

    period = PaymentPeriod(
        accrual_start=date(2026, 1, 1),
        accrual_end=date(2027, 1, 1),
        payment_date=date(2027, 1, 1),
    )

    assert period.accrual_start == date(2026, 1, 1)
    assert period.accrual_end == date(2027, 1, 1)
    assert period.payment_date == date(2027, 1, 1)


def test_accrual_days():

    period = PaymentPeriod(
        accrual_start=date(2026, 1, 1),
        accrual_end=date(2027, 1, 1),
        payment_date=date(2027, 1, 1),
    )

    assert period.accrual_days == 365


def test_invalid_accrual_dates():

    with raises(ValueError):

        PaymentPeriod(
            accrual_start=date(2027, 1, 1),
            accrual_end=date(2026, 1, 1),
            payment_date=date(2027, 1, 1),
        )


def test_invalid_payment_date():

    with raises(ValueError):

        PaymentPeriod(
            accrual_start=date(2026, 1, 1),
            accrual_end=date(2027, 1, 1),
            payment_date=date(2026, 12, 31),
        )