import tkinter as tk
root = tk.Tk()
root.title("Form")

def display():
    name = entry_name.get()
    age = entry_age.get()
    with open("application.txt", "a") as file:
        file.write(f"Name: {name}\nAge: {age}\n")
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Application submitted", font=("Arial", 14)).pack(padx=20, pady=40)

tk.Label(root, text = "Name").grid(row = 0, column = 0, padx = 10, pady = 10)
entry_name = tk.Entry(root)
entry_name.grid(row = 0, column = 1, padx = 10, pady = 10)

tk.Label(root, text = "Age").grid(row = 1, column = 0, padx = 10, pady = 10)
entry_age = tk.Entry(root)
entry_age.grid(row = 1, column = 1, padx = 10, pady = 10)

tk.Button(root, text = "Submit", command=display).grid(row = 2, column = 0, padx = 10, pady = 10)

root.mainloop()