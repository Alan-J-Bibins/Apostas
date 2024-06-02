"""
Python module that defines the Task class that Apostas uses
"""

from dependencies.date_handler import DateHandler as date_handler


class Task:
    """
    Task object
    """
    def __init__(self, topic:str, topic_id=0,datestr=""):
        self.topic: str = topic
        self.topic_id = topic_id
        self.date_handler: date_handler = date_handler(datestr)
