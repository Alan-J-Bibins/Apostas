from dependencies.task_handler import TaskHandler

def main():
    cog()

def cog():
    choice = int(input("[1]Add New Topic\n[2]Get Topic List for the day\nEnter:"))
    task_handler_obj = TaskHandler()
    match(choice):
        case 1:
            task_handler_obj.make_new_task()
        # case 2:
            # task_handler_obj.create_task_list()
    task_handler_obj.db_handler.close_connection()

if __name__ == "__main__":
    main()
