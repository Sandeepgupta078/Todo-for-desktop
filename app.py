import tkinter as tk
from tkinter import messagebox

# Functionality for the To-Do App
def add_task():
    task = task_input.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = tasks_listbox.curselection()
        tasks_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def clear_all_tasks():
    tasks_listbox.delete(0, tk.END)

# GUI for To-Do App
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="To-Do List App", font=("Helvetica", 16, "bold"), pady=10)
heading.pack()

# Input Task Frame
frame = tk.Frame(root)
frame.pack(pady=10)

task_input = tk.Entry(frame, width=30, font=("Helvetica", 12))
task_input.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 10), bg="#4CAF50", fg="white")
add_button.pack(side=tk.LEFT)

# Task List Box
tasks_listbox = tk.Listbox(root, width=45, height=12, font=("Helvetica", 12), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Action Buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 10))
delete_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(buttons_frame, text="Clear All Tasks", command=clear_all_tasks, bg="#FF9800", fg="white", font=("Helvetica", 10))
clear_button.grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
