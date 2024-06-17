# Task Management System

tasks = []

def display_menu():
    """
    Displays the menu for the user to choose an option.
    """
    print("\nTask Management System")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. Delete a task")
    print("4. Display all tasks")
    print("5. Exit")

def add_task():
    """
    Prompts the user to enter a new task and adds it to the list.
    """
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def mark_completed():
    """
    Displays all tasks and prompts the user to select a task to mark as completed.
    """
    if not tasks:
        print("No tasks to mark as completed.")
        return

    print("Select a task to mark as completed:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {'Completed' if task['completed'] else 'Pending'}")

    choice = int(input("Enter the task number: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid choice.")

def delete_task():
    """
    Displays all tasks and prompts the user to select a task to delete.
    """
    if not tasks:
        print("No tasks to delete.")
        return

    print("Select a task to delete:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {'Completed' if task['completed'] else 'Pending'}")

    choice = int(input("Enter the task number: "))
    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid choice.")

def display_tasks():
    """
    Displays all tasks with their completion status.
    """
    if not tasks:
        print("No tasks to display.")
        return

    print("All Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {'Completed' if task['completed'] else 'Pending'}")

def main():
    """
    The main function that runs the program.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()