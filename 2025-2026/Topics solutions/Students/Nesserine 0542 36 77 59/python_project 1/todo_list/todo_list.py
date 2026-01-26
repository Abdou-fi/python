import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List Manager")
        self.root.geometry("500x400")
        self.root.resizable(True, True)
    
        self.tasks_file = "tasks.json"
        self.tasks = self.load_tasks()
       
        self.setup_ui()
        self.update_task_list()
   
    def setup_ui(self):
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X, padx=10, pady=5)
       
        ttk.Label(input_frame, text="New Task:").pack(side=tk.LEFT)
        self.task_entry = ttk.Entry(input_frame, width=30, font=('Arial', 10))
        self.task_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.task_entry.bind('<Return>', lambda e: self.add_task())
       
        ttk.Button(input_frame, text="Add Task",
                  command=self.add_task).pack(side=tk.RIGHT, padx=5)
       
        list_frame = ttk.Frame(self.root, padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
       
        ttk.Label(list_frame, text="Your Tasks:",
                 font=('Arial', 12, 'bold')).pack(anchor=tk.W)
       
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
        self.task_listbox = tk.Listbox(list_frame,
                                     yscrollcommand=scrollbar.set,
                                     font=('Arial', 10),
                                     selectmode=tk.SINGLE,
                                     height=12)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
       
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X, padx=10, pady=5)
       
        ttk.Button(button_frame, text="Delete Selected",
                  command=self.delete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All",
                  command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save Tasks",
                  command=self.save_tasks).pack(side=tk.RIGHT, padx=5)
   
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
   
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks.pop(index)
            self.update_task_list()
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
   
    def clear_all(self):
        if self.tasks and messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.tasks.clear()
            self.update_task_list()
            self.save_tasks()
   
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, 1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")
   
    def save_tasks(self):
        try:
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception:
            pass  
    def load_tasks(self):
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return []

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()