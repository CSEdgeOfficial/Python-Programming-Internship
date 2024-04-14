import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        
        self.tasks = []

        self.task_name_label = tk.Label(master, text="Task Name:")
        self.task_name_label.grid(row=0, column=0)
        self.task_name_entry = tk.Entry(master)
        self.task_name_entry.grid(row=0, column=1)

        self.task_desc_label = tk.Label(master, text="Task Description:")
        self.task_desc_label.grid(row=1, column=0)
        self.task_desc_entry = tk.Entry(master)
        self.task_desc_entry.grid(row=1, column=1)

        self.task_due_label = tk.Label(master, text="Due Date:")
        self.task_due_label.grid(row=2, column=0)
        self.task_due_entry = tk.Entry(master)
        self.task_due_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=4, column=0, columnspan=2)

    def add_task(self):
        name = self.task_name_entry.get()
        description = self.task_desc_entry.get()
        due_date = self.task_due_entry.get()
        task = Task(name, description, due_date)
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, f"Name: {name}, Description: {description}, Due Date: {due_date}")

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
