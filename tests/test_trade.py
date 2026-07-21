from datetime import date

import pytest

from src.products.trade import Trade


def test_trade_creation():

    trade = Trade(
        trade_id="IRS001",
        counterparty="Goldman Sachs",
        currency="USD",
        effective_date=date(2026, 1, 1),
        maturity_date=date(2031, 1, 1),
    )

    assert trade.trade_id == "IRS001"
    assert trade.currency == "USD"


def test_empty_trade_id():

    with pytest.raises(ValueError):
        Trade(
            trade_id="",
            counterparty="GS",
            currency="USD",
            effective_date=date(2026, 1, 1),
            maturity_date=date(2031, 1, 1),
        )


def test_empty_counterparty():

    with pytest.raises(ValueError):
        Trade(
            trade_id="IRS001",
            counterparty="",
            currency="USD",
            effective_date=date(2026, 1, 1),
            maturity_date=date(2031, 1, 1),
        )


def test_invalid_currency():

    with pytest.raises(ValueError):
        Trade(
            trade_id="IRS001",
            counterparty="GS",
            currency="US",
            effective_date=date(2026, 1, 1),
            maturity_date=date(2031, 1, 1),
        )


def test_invalid_dates():

    with pytest.raises(ValueError):
        Trade(
            trade_id="IRS001",
            counterparty="GS",
            currency="USD",
            effective_date=date(2031, 1, 1),
            maturity_date=date(2026, 1, 1),
        )