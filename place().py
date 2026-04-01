import tkinter as tk
root = tk.Tk()
root.title("Form Example with place()")

def display():
    name = entry.get()
    label.config(text=f"Hello {name}")

entry = tk.Entry(root)
entry.place(x=100, y=100)

Button = tk.Button(root, text="Submit", command=display)
Button.place(x=100, y=150)

label = tk.Label(root, text="Enter your name")
label.place(x=100, y=200)

root.mainloop()
