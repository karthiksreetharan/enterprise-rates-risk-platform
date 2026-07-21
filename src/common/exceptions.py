"""
exceptions.py

Custom exception hierarchy for the interest rate risk platform.
"""

from __future__ import annotations


class PricingPlatformError(Exception):
    """
    Base exception for the entire platform.
    """

    pass


# ---------------------------------------------------------------------
# Market Data
# ---------------------------------------------------------------------

class MarketDataError(PricingPlatformError):
    """
    Raised for invalid market data.
    """

    pass


class DuplicateQuoteError(MarketDataError):
    """
    Raised when duplicate market quotes are supplied.
    """

    pass


class InvalidQuoteError(MarketDataError):
    """
    Raised when a market quote is invalid.
    """

    pass


# ---------------------------------------------------------------------
# Instruments
# ---------------------------------------------------------------------

class InstrumentError(PricingPlatformError):
    """
    Raised for invalid financial instruments.
    """

    pass


# ---------------------------------------------------------------------
# Curves
# ---------------------------------------------------------------------

class CurveError(PricingPlatformError):
    """
    Raised for curve-related errors.
    """

    pass


class BootstrapError(CurveError):
    """
    Raised when curve bootstrapping fails.
    """

    pass


class InterpolationError(CurveError):
    """
    Raised for interpolation failures.
    """

    pass


class CurveRangeError(CurveError):
    """
    Raised when requested maturity lies outside
    the available curve range.
    """

    pass


# ---------------------------------------------------------------------
# Schedule Generation
# ---------------------------------------------------------------------

class ScheduleError(PricingPlatformError):
    """
    Raised for schedule generation failures.
    """

    pass


# ---------------------------------------------------------------------
# Day Count
# ---------------------------------------------------------------------

class DayCountError(PricingPlatformError):
    """
    Raised for invalid day count calculations.
    """

    pass


# ---------------------------------------------------------------------
# Pricing
# ---------------------------------------------------------------------

class PricingError(PricingPlatformError):
    """
    Raised during valuation.
    """

    pass


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

class ValidationError(PricingPlatformError):
    """
    Raised when validation fails.
    """

    pass