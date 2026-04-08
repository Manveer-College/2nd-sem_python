import tkinter as tk
root = tk.Tk()
root.title("Welcome")
root.geometry("300x200")

def signup():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Signup Program")
    # name
    lb_name = tk.Label(root, text="Name")
    lb_name.grid(row=0, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1)
    # email
    lb_email = tk.Label(root, text="Email")
    lb_email.grid(row=1, column=0)
    entry_email = tk.Entry(root)
    entry_email.grid(row=1, column=1)
    # password
    lb_password = tk.Label(root, text="Password")
    lb_password.grid(row=2, column=0)
    entry_password = tk.Entry(root)
    entry_password.grid(row=2, column=1)
    # signup button
    btn_signup = tk.Button(root, text="Signup")
    btn_signup.grid(row=3, column=0, columnspan=2)

    #already have a account
    lb_already_have_account = tk.Label(root, text="Already have a account? Login here")
    lb_already_have_account.grid(row=4, column=0, columnspan=2)
    # login button
    btn_login = tk.Button(root, text="Login", command=login)
    btn_login.grid(row=5, column=0, columnspan=2)


def login():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Login Program")
    #email
    lbl_email = tk.Label(root, text = "Email")
    lbl_email.grid(row = 0, column = 0)
    entryl_email = tk.Entry(root)
    entryl_email.grid(row = 0, column = 1)
    #password
    lbl_password = tk.Label(root, text = "Password")
    lbl_password.grid(row = 1, column = 0)
    entryl_password = tk.Entry(root)
    entryl_password.grid(row = 1, column = 1)
    lbutton = tk.Button(root, text = "Login")
    lbutton.grid(row = 2, column = 0, columnspan = 2)
    #already have a account
    lb_already_have_account = tk.Label(root, text="Don't have a account? Signup here")
    lb_already_have_account.grid(row=3, column=0, columnspan=2)
    # login button
    btn_login = tk.Button(root, text="Signup", command=signup)
    btn_login.grid(row=4, column=0, columnspan=2)

signup()
root.mainloop()