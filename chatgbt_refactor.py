def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks available!")
    else:
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    if not todo_list:
        print("No tasks available!")
    else:
        task = input("Choose the task: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")

def main():
    todo_list = []

    while True:
        user = input("Choose a command (add, view, remove, exit): ")

        if user == "add":
            add_task(todo_list)

        elif user == "view":
            view_tasks(todo_list)

        elif user == "remove":
            remove_task(todo_list)

        elif user == "exit":
            break

        else:
            print("Invalid command. Please enter 'add', 'view', 'remove', or 'exit'.")

if __name__ == "__main__":
    main()
