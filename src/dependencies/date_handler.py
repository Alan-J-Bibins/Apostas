"""
Python module that deals with handling dates using the datetime builtin module of python

"""

from datetime import date as d
from datetime import timedelta


class DateHandler:
    """
    Handler for date using the date and timedelta class from the builtin datetime module of python
    """

    def __init__(self, datestr: str = ""):
        self.date = d.today() if datestr == "" else d.fromisoformat(datestr)

    def update_date(self):
        """
        Updates self.dateobj to current date
        """
        self.date = d.today()

    def return_diff(self, other_date: d) -> int:
        """
        Returns difference between two date objects as days
        """
        diff: timedelta = other_date - self.date
        return diff.days
