"""
enums.py

Enumerations used throughout the interest rate risk platform.
"""

from __future__ import annotations

from enum import Enum


class InstrumentType(str, Enum):
    """
    Supported market instruments.
    """

    DEPOSIT = "Deposit"
    SWAP = "Swap"


class Currency(str, Enum):
    """
    Supported currencies.
    """

    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"


class Frequency(str, Enum):
    """
    Payment frequency.
    """

    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMI_ANNUAL = "SemiAnnual"
    ANNUAL = "Annual"


class DayCountConvention(str, Enum):
    """
    Supported day count conventions.
    """

    ACTUAL_360 = "ACT/360"
    ACTUAL_365 = "ACT/365"
    THIRTY_360 = "30/360"


class BusinessDayConvention(str, Enum):
    """
    Business day adjustment rules.
    """

    FOLLOWING = "Following"
    MODIFIED_FOLLOWING = "Modified Following"
    PRECEDING = "Preceding"
    MODIFIED_PRECEDING = "Modified Preceding"
    UNADJUSTED = "Unadjusted"


class PayReceive(str, Enum):
    """
    Swap direction.
    """

    PAY = "Pay"
    RECEIVE = "Receive"


class Compounding(str, Enum):
    """
    Interest compounding conventions.
    """

    SIMPLE = "Simple"
    CONTINUOUS = "Continuous"


class InterpolationMethod(str, Enum):
    """
    Curve interpolation methods.
    """

    LINEAR = "Linear"