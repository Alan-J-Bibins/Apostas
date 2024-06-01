from dependencies.task import Task
from dependencies.db import db


class TaskHandler:
    """
    Class that handles creation of tasks along with operations for them
    """

    def __init__(self):
        self.db_handler = db()
        self.db_handler.create_table(
            "Topic",
            "topic_id INT PRIMARY KEY AUTO_INCREMENT, topic TEXT, date_created VARCHAR(255), daydelta INT",
        )

    def make_new_task(self):
        """
        Makes new task and adds it to database
        """
        topic = input("Enter topic: ")
        task_obj = Task(topic)
        print(
            f"DEBUG: {task_obj.topic} {task_obj.date_handler.strdate} {task_obj.date_handler.daydiff}"
        )
        self.db_handler.insert_data(
            "Topic",
            task_obj.topic,
            task_obj.date_handler.strdate,
            task_obj.date_handler.daydiff,
        )

    def delete_task(self):
        """
        Deletes task from database
        """

    def create_task_list(self):
        """
        Creates list topics to be studied for the day
        """
