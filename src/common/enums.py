"""
enums.py

Common enumerations used across the project.
"""

from enum import Enum


class PayReceive(Enum):
    PAY = "PAY"
    RECEIVE = "RECEIVE"


class DayCountConvention(Enum):
    ACT_365 = "ACT/365"


class PaymentFrequency(Enum):
    ANNUAL = 1
    SEMI_ANNUAL = 2
    QUARTERLY = 4
    MONTHLY = 12


class FloatingIndex(Enum):
    SOFR = "SOFR"
    LIBOR_3M = "LIBOR 3M"