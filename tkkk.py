import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Test program")
root.geometry("500x500")
label = tk.Label(root, text="Hello World")
label.pack()

entry = tk.Entry(root)
entry.pack()

def show_text():
    label.config(text=entry.get())

button = tk.Button(root, text="Show Text", command=show_text)
button.pack()

var = tk.IntVar()
check = tk.Checkbutton(root, text="Accept", variable = var)
check.pack()    

frame = tk.Frame(root, bg = "yellow", padx = 10, pady = 10)
frame.pack()
tk.Label(frame, text="Test 1").pack()

listbox = tk.Listbox(frame)
listbox.pack()

listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")

scoll = tk.Scrollbar(frame)
scoll.pack()

canvas = tk.Canvas(root, width = 50, height = 50, bg = "red")
canvas.pack()
canvas.create_rectangle(10, 10, 100, 100, fill = "blue")

mb = tk.Menubutton(root, text = "Options")
mb.pack()

menu = tk.Menu(mb)
mb.config(menu = menu)

menu.add_command(label = "Option 1")
menu.add_command(label = "Option 2")
menu.add_command(label = "Option 3")

r1 = tk.Radiobutton(root, text = "male", variable = var, value = 1)
r1.pack()
r2 = tk.Radiobutton(root, text = "female", variable = var, value = 2)
r2.pack()

top = tk.Toplevel(root)
top.geometry("300x300")
top.title("Top Level")
label = tk.Label(top, text = "This is a top level window")
label.pack()

labelff = tk.LabelFrame(top, text = "Label Frame")
labelff.pack()

tk.Entry(labelff).pack()
spin= tk.Spinbox(labelff, from_ = 0, to = 100)
spin.pack()

progress = ttk.Progressbar(top)
progress.pack()
progress['value'] = 40

text = tk.Text(top)
text.pack()


from tkinter import messagebox
messagebox.showinfo("Info", "This is a message")
root.mainloop()