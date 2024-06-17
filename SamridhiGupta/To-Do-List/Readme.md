# Task Management System

## Overview

This is a simple Python program to manage tasks. Users can add tasks, mark tasks as completed, delete tasks, and view all tasks with their completion status.

## Features

- **Add Task**: Allows the user to add a new task to the list.
- **Mark Task as Completed**: Allows the user to mark a specific task as completed.
- **Delete Task**: Allows the user to delete a specific task from the list.
- **Display All Tasks**: Displays all tasks along with their completion status.
- **Exit Program**: Allows the user to exit the program.

## How to Use

1. **Run the Program**: Execute the script to start the task management system.
2. **Choose an Option**: Follow the on-screen menu to choose an option by entering the corresponding number.
3. **Follow Prompts**: Enter the required information based on the chosen option (e.g., task details, task number).
4. **View Results**: The program will display appropriate messages based on the action performed.

### Example Usage

1. **Adding a Task**:
    ```
    Task Management System
    1. Add a task
    2. Mark a task as completed
    3. Delete a task
    4. Display all tasks
    5. Exit
    Enter your choice (1-5): 1
    Enter a new task: Buy groceries
    Task added successfully.
    ```

2. **Marking a Task as Completed**:
    ```
    Task Management System
    1. Add a task
    2. Mark a task as completed
    3. Delete a task
    4. Display all tasks
    5. Exit
    Enter your choice (1-5): 2
    Select a task to mark as completed:
    1. Buy groceries - Pending
    Enter the task number: 1
    Task marked as completed.
    ```

3. **Deleting a Task**:
    ```
    Task Management System
    1. Add a task
    2. Mark a task as completed
    3. Delete a task
    4. Display all tasks
    5. Exit
    Enter your choice (1-5): 3
    Select a task to delete:
    1. Buy groceries - Completed
    Enter the task number: 1
    Task deleted successfully.
    ```

4. **Displaying All Tasks**:
    ```
    Task Management System
    1. Add a task
    2. Mark a task as completed
    3. Delete a task
    4. Display all tasks
    5. Exit
    Enter your choice (1-5): 4
    All Tasks:
    No tasks to display.
    ```
## Error Handling
The program includes basic error handling to manage common issues:

1. **Empty Task List:**

If there are no tasks to mark as completed, delete, or display, the program will display appropriate messages: No tasks to mark as completed., No tasks to delete., and No tasks to display.

2. **Invalid Task Number:**

If the user enters an invalid task number for marking as completed or deleting, the program will display the message: Invalid choice.

3. **Invalid Menu Choice:**

If the user enters a choice outside the range of 1-5, the program will display the message: Invalid choice. Please try again.