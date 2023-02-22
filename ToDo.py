import tkinter as tk

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        list_tasks.delete(0, tk.END)
        for i, task in enumerate(tasks, 1):
            list_tasks.insert(tk.END, f"{i}. {task}")
        entry_task.delete(0, tk.END)

def remove_task():
    task_index = list_tasks.curselection()
    if task_index:
        tasks.pop(task_index[0])
        list_tasks.delete(task_index)
    else:
        tk.messagebox.showwarning("Warning", "Please select a task to remove.")

def view_all_tasks():
    if tasks:
        tk.messagebox.showinfo("To-Do List", "\n".join(tasks))
    else:
        tk.messagebox.showinfo("To-Do List", "No tasks found.")

def add_homework():
    tasks.append("Do homework")
    list_tasks.insert(tk.END, f"{len(tasks)}. Do homework")

def add_dog():
    tasks.append("Take the dog outside")
    list_tasks.insert(tk.END, f"{len(tasks)}. Take the dog outside")

def add_clean():
    tasks.append("Clean up room")
    list_tasks.insert(tk.END, f"{len(tasks)}. Clean up room")

def clickExitButton():
    exit()

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

my_font = ("times", 22, 'bold')
my_font2 = ("times", 15, 'bold')

label_hello = tk.Label(text="To-Do List App", font=my_font)
label_hello.pack(side=tk.TOP)
label_credits = tk.Label(text="BBC gaming", font=my_font2)
label_credits.pack(side=tk.TOP)

exitButton = tk.Button( text="Exit", command=clickExitButton)

# Create the user interface
frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

label_task = tk.Label(frame_input, text="Enter task:")
label_task.pack(side=tk.LEFT)

entry_task = tk.Entry(frame_input, width=50)
entry_task.pack(side=tk.LEFT)

button_add = tk.Button(root, text="Add task", command=add_task)
button_add.pack(side=tk.TOP, padx=10, pady=10)

button_remove = tk.Button(root, text="Remove task", command=remove_task)
button_remove.pack(side=tk.TOP, padx=10, pady=10)

#Label for quick selet
hello_label = tk.Label(root, text="Quick select\n-------------------------------------------------------------------------------")
hello_label.pack(side=tk.TOP, padx=10, pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.TOP, padx=10, pady=10)

#Quick add section
button_homework = tk.Button(frame_buttons, text="Add homework", command=add_homework)
button_homework.pack(side=tk.LEFT, padx=10)

button_dog = tk.Button(frame_buttons, text="Take the dog outside", command=add_dog)
button_dog.pack(side=tk.LEFT, padx=10)

button_clean = tk.Button(frame_buttons, text="Clean up room", command=add_clean)
button_clean.pack(side=tk.LEFT, padx=10)

frame_list = tk.Frame(root)
frame_list.pack(side=tk.TOP, padx=10, pady=10)

list_tasks = tk.Listbox(frame_list, height=10, width=50)
list_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_list)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

#set ups a scroll wheel to view all your tasks
list_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=list_tasks.yview)

# Start the event loop
root.mainloop()
