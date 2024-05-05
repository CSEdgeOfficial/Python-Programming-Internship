import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=5, pady=10)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index] += " - Completed"
            self.task_listbox.delete(index)
            self.task_listbox.insert(tk.END, self.tasks[index])
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def main():
    root = tk.Tk()
    todo_app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
