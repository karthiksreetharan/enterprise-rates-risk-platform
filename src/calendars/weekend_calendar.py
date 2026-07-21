"""
weekend_calendar.py

Weekend calendar utilities.
"""

from __future__ import annotations

from datetime import date


class WeekendCalendar:
    """
    Utility class for weekend calculations.

    Python weekday():

    Monday      = 0
    Tuesday     = 1
    Wednesday   = 2
    Thursday    = 3
    Friday      = 4
    Saturday    = 5
    Sunday      = 6
    """

    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(
        day: date,
    ) -> bool:
        """
        Return True if the supplied date falls on a weekend.
        """

        return day.weekday() in WeekendCalendar.WEEKEND_DAYS

    @staticmethod
    def is_business_day(
        day: date,
    ) -> bool:
        """
        Return True if the supplied date is a business day.
        """

        return not WeekendCalendar.is_weekend(day)