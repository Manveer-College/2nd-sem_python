import tkinter as tk
root = tk.Tk()
root.title("Form Example with grid()")

tk.Label(root, text = "Name").grid(row = 0, column = 0, padx = 10, pady = 10)
tk.Entry(root).grid(row = 0, column = 1, padx = 10, pady = 10)

tk.Label(root, text = "Age").grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Entry(root).grid(row = 1, column = 1, padx = 10, pady = 10)

tk.Button(root, text = "Submit").grid(row = 2, column = 0, padx = 10, pady = 10)

root.mainloop()