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

    def delete_task(self):
        """
        Deletes task from database
        """

    def update_db_daydelta(self):
        """
        Updates daydelta column
        """
        topics_in_db = self.db_handler.query_db("Topic", "topic, topic_id, date_created")
        print(topics_in_db)
        list_of_tasks = []
        for data in topics_in_db:
            list_of_tasks.append(Task(data[0],data[1],data[2]))

        for i in range(len(list_of_tasks)):
            self.db_handler.update_data("Topic","daydelta",list_of_tasks[i].date_handler.update(), "topic_id", list_of_tasks[i].topic_id)




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
        self.update_db_daydelta()

    def create_task_list(self):
        """
        Makes List of topics to revise
        """
        self.update_db_daydelta()
        spacing_intervals = [1,3,7,16,32,66]
        topic_query = self.db_handler.query_db("Topic")
        task_list = []
        for data in topic_query:
            if data[3] in spacing_intervals:
                print("heloo there")
                task_list.append(data[1])
        print("Tasks for today:")
        print(task_list)


