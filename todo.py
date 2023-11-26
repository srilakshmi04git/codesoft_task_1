import tkinter as tk

class ToDoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=30)
        self.task_listbox.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_as_done)
        self.mark_done_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                index = selected_task_index[0]
                self.tasks[index] = {"task": new_task, "done": False}
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, new_task)
                self.task_entry.delete(0, tk.END)

    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["done"] = True
            task = self.tasks[index]["task"]
            self.task_listbox.delete(index)
            self.task_listbox.insert(tk.END, f"{task} (Done)")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["done"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['task']} ({status})")

if __name__ == "_main_":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
