from dependencies.task_handler import TaskHandler

def main():
    task_handler_obj = TaskHandler()
    task_handler_obj.create_task_list()
    cog(task_handler_obj)
    task_handler_obj.db_handler.close_connection()

def cog(task_handler_obj):
    choice = int(input("[1]Add New Topic\n[2]Exit\nEnter:"))
    while(choice != 2):
        match(choice):
            case 1:
                task_handler_obj.make_new_task()
            case 2:
                break

if __name__ == "__main__":
    main()
