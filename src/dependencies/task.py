"""
Python module that defines the Task class that Apostas uses
"""

from date_handler import DateHandler as date_handler


class Task:
    """
    Task object
    """
    def __init__(self):
        self.topic: str = ""
        self.date_handler: date_handler = date_handler()
