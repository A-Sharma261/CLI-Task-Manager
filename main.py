import json

# creates a menu which is repeatable after every action
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


# add tasks to the tasks.json file
def add_task():
    task = input("\n\n\nEnter the name of your TASK: \n")
    while True:
        print("\nDo you wish to call the new task: "+ task)
        checker = input("").lower()
        if checker == "yes" or checker == "y":
            break
        elif checker == "no" or checker == "n":
            add_task()
            break
        else:
            print("This is an invalid input please try again")
            continue

    new_task = {"Task": task, "Status": "Incomplete"}          #the structure of the dictionary within the list of the json

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(new_task)

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\n\nTask added successfully!")

    while True:
        repeat = input("Do you wish to add another task \n").lower()
        if repeat == "yes" or repeat == "y":
            add_task()
            break
        elif repeat == "no" or repeat == "n":
            break
        else:
            print("\nThis is not a valid input reply with 'yes' or 'no' thank you. \n")
            continue
    

def view_task():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\n\n\nThere are currently no tasks. Please add task to view them.")
        return []

    count = 1
    for i in data:
        print(f"\n{count}. task: {i['Task']} | Status: {i['Status']}")
        count = count + 1
    
    


def status_change():
    view_task()
    while True:

#Mostly error proofing
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        index = input("\nWhich task number do you wish to mark as done: ")
        try:
            index = int(index)
        except ValueError:
            print("This is not a valid number. Please try again.")
            continue

        if int(index) > len(data) or int(index ) <= 0:
            print("A task with this number does not exist. Please try again.")
            continue

        #actual work of changing status
        task = data[index - 1]
        task_name = task['Task']
        status = task['Status']
        print("\n\nThe Current status for the task: '" + task_name + "' is " + status.upper())

        while True:
            if status.lower() == "complete":
                status_incomplete = input("Do you wish to change the status of this task to INCOMPLETE ").lower()
                if status_incomplete == "yes" or status_incomplete == "y":
                    task['Status'] = "Incomplete"
                    break
                elif status_incomplete == "no" or status_incomplete == "n":
                    break
                else:
                    print("This is not a valid input reply with 'yes' or 'no' thank you. ")
                    continue
            elif status.lower() == "incomplete":
                status_complete = input("Do you wish to change the status of this task to COMPLETE ").lower()
                if status_complete == "yes" or status_complete == "y":
                    task['Status'] = "Complete"
                    break
                elif status_complete == "no" or status_complete == "n":
                    break
                else:
                    print("This is not a valid input reply with 'yes' or 'no' thank you. ")
                    continue


#save changes
        try:
            with open("tasks.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"\n\nTask '{task_name}' status updated to '{task['Status']}'.")
        except Exception as e:
            print(f"Error saving the file: {e}")

#repeat question
        while True:
            repeat = input("Do you wish to change another task? ").lower()
            if repeat == "yes" or repeat == "y":
                status_change()
                break
            elif repeat == "no" or repeat == "n":
                break
            else:
                print("\n\nInvalid input. Please reply with 'yes' or 'no'.")
                continue
        break


def delete_task():
    view_task()
    while True:

        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        index = input("\nWhich task number do you wish to delete: ")
        try:
            index = int(index)
        except ValueError:
            print("This is not a valid number. Please try again.")
            continue

        if int(index) > len(data) or int(index ) <= 0:
            print("A task with this number does not exist. Please try again.")
            continue

        #actual work of changing status
        task = data[index - 1]
        task_name = task['Task']
        while True: 
            checker = input("The task you wish to delete is?: '" + task_name +"'. Do you wish to delete it: ").lower()
            if checker == "yes" or checker == "y":
                del data[index - 1]
                break
            elif checker == "no" or checker == "n":
                break
            else:
                print("\n\nInvalid input. Please reply with 'yes' or 'no'.")
                continue
        

#save changes
        try:
            with open("tasks.json", "w") as file:
                json.dump(data, file, indent=4)
                print("This task has been successfully DELETED")
        except Exception as e:
            print(f"Error saving the file: {e}")

#repeat question
        while True:
            repeat = input("\nDo you wish to delete another task?: ").lower()
            if repeat == "yes" or repeat == "y":
                delete_task()
                break
            elif repeat == "no" or repeat == "n":
                break
            else:
                print("Invalid input. Please reply with 'yes' or 'no'.")
                continue
        break




while True:
    choice = menu()

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
        exit = input("\n\nInput anything to exit: ")
    elif choice == 3:
        status_change()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Goodbye!")
        break



