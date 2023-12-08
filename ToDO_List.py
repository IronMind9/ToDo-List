todo_list = []

while True:
    user = input("Choose a command (add, view, remove, exit): ")

    if user == "add":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif user == "view":
        if not todo_list:
            print("No tasks available!")
        else:
            for task in todo_list:
                print(task)

    elif user == "remove":
        if not todo_list:
            print("No tasks available!")
        else:
            task = input("Choose the task: ")
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed successfully!")
            else:
                print("Task not found!")

    elif user == "exit":
        break
    else:
        print("Invalid command. Please enter 'add', 'view', 'remove', or 'exit'.")

        
    
    
               
        
        
            

    
    
       