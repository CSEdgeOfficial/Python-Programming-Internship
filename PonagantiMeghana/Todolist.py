import json
import os
def display_menu():
    print("Todo List Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
def todolist():
    tasks = []

    while 1:
        display_menu()
        ch= input("Enter your choice btw 1 and 4: ")

        if ch== "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added.")

        elif ch == "2":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")

                
        elif ch== "3":
            print("Tasks are:")
            if tasks:
                for index ,task in enumerate(tasks,start=1):
                    print(f"{index}. {task}")
            else:
                print("no tasks added")
        elif ch == "4":
            break

        else:
            print("Invalid choice. Please try again.")
todolist()