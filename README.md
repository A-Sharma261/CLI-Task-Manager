Task Manager CLI Application
Overview

This is a Command-Line Interface (CLI) Task Manager built in Python that allows users to manage tasks. It allows users to:

Add tasks
View tasks
Mark tasks as completed or incomplete
Delete tasks

The tasks are stored in a JSON file, ensuring persistence between sessions.

Features
Add Task: Users can add new tasks to the task list.
View Tasks: Users can view all the tasks along with their current status.
Change Status: Users can mark a task as complete or incomplete.
Delete Task: Users can delete tasks from the list.
Repeat Actions: After any action, users are prompted to continue or exit the task management process.
Installation
Clone the repository or download the Python script.
Ensure you have Python 3.x installed on your machine.
You will need to have access to a terminal (Command Prompt, PowerShell, or any Linux terminal).
How to Use
Run the Program:
In the terminal, navigate to the directory where the Python file is located.

Run the script using the command:

python task_manager.py
Menu Options:

When you run the program, you will be prompted with the following menu options:

1. Add task
2. View tasks
3. Mark task as done
4. Delete task
5. Exit
Adding a Task:
Select the "Add task" option (Option 1).
Enter the name of the task when prompted.
You can continue adding tasks or exit.
Viewing Tasks:
Select the "View tasks" option (Option 2).
The tasks will be displayed along with their status (incomplete/complete).
Changing the Status of a Task:
Select the "Mark task as done" option (Option 3).
You will be asked to choose a task by its number and whether you want to mark it as complete or incomplete.
Deleting a Task:
Select the "Delete task" option (Option 4).
Confirm the task to delete, and it will be removed from the task list.
Exiting the Program:
Select the "Exit" option (Option 5) to exit the program.
File Storage
All tasks are stored in a JSON file called tasks.json.
The file contains a list of tasks, each with a Task (task name) and Status (either "Incomplete" or "Complete").
Error Handling
If the tasks.json file is missing or corrupted, the program will create a new file and continue running.
If the user provides invalid input, the program will prompt them to try again.
Example Interaction:
==== CLI Task Manager ====
1. Add task
2. View tasks
3. Mark task as done
4. Delete task
5. Exit

Enter Your Choice: 1
Enter the name of your TASK: Learn Python
Do you wish to call the new task: Learn Python (yes/no): yes
Task added successfully!

Do you wish to add another task (yes/no): no
Future Improvements
Implement task due dates and priority levels.
Enhance task searching and filtering.
Add support for task categories.