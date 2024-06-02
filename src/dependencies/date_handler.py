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
        self.strdate = self.date.strftime("%Y-%m-%d")
        self.daydiff = 0

    def update(self):
        """
        updates daydiff
        """
        other_date: d = d.today()
        diff: timedelta = other_date - self.date
        self.daydiff = diff.days
        return self.daydiff
