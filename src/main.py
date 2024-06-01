from dependencies.task_handler import TaskHandler

def main():
    cog()

def cog():
    choice = int(input("[1]Add New Topic\nEnter:"))
    task_handler_obj = TaskHandler()
    match(choice):
        case 1:
            task_handler_obj.make_new_task()

if __name__ == "__main__":
    main()
