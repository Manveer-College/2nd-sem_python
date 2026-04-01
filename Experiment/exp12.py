import tkinter as tk
root = tk.Tk()
root.title("Form Example")

def display():
    name = entry.get()
    label.config(text=f"Hello {name}")

entry = tk.Entry(root)
entry.pack(pady=10)

Button = tk.Button(root, text="Submit", command=display)
Button.pack()

label = tk.Label(root, text="Enter your name")
label.pack()

root.mainloop()
