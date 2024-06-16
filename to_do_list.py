class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index")

    def display_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i+1}. {task['task']} - {status}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == "2":
            index = int(input("Enter the index of the task to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            task_manager.mark_task_completed(index)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
