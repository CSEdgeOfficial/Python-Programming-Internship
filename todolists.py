import json
import os

def display_menu():
    print("Todo List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added.")

        elif choice == "2":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == "3":
            print("Tasks:")
            for task in tasks:
                print("- " + task)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
