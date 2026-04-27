import json

def menu():
    while True:
        print("""\n\n\n==== CLI Task Manager ====
    1. Add task
    2. View tasks
    3. Mark task as done
    4. Delete task
    5. Exit""")

        choice = input("Enter Your Choice: ").strip().lower()

        match choice:
            case "1" | "add" | "addtask":
                return 1
            case "2" | "view" | "viewtask":
                return 2
            case "3" | "mark" | "marktask" | "marktaskasdone":
                return 3
            case "4" | "delete" | "deletetask":
                return 4
            case "5" | "exit":
                return 5
            case _:
                print("\n\n\nThis is an incorrect input, please try again")


import json

def add_task():
    task = input("\n\n\nEnter the name of your TASK: ")
    new_task = {"Task": task, "Status": False}
    
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(new_task)

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Task added successfully!")

def view_task():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    for i in data:
        task = i['Task']
        status = i['Status']
        if status:
            status = "True"
        else:
            status = "False"
        print("\n\n\ntask: " + task + " | Status: " + status)


def mark_done():
    
    view_task()
    while True:
        index = input("\nWhich task do you wish to mark as done: ")
        







while True:
    choice = menu()

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        print("Mark task not built yet")
    elif choice == 4:
        print("Delete task not built yet")
    elif choice == 5:
        print("Goodbye!")
        break



