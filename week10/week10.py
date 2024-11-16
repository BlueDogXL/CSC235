
# root = tk.Tk()
# root.title("python week 10 widget")
# label = tk.Label(root, text = "Hello World")
# label.pack()

# def onClick():
#     print("Button clicked!")

# button = tk.Button(root, text = "Click here!", command = onClick)
# button.pack()
# root.mainloop() # keeps the program running and listens for events

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login")
root.geometry("300x400")
loginTitle = tk.Label(root, text = "Login").pack()
correctUsername = "BlueDogXL"
correctPassword = "12345"

def submitLogin():
    username = usernameField.get()
    password = passwordField.get()
    if username == correctUsername and password == correctPassword:
        messagebox.showinfo(title = "Success", message = f"Welcome, {username}!")
    else:
        messagebox.showerror(title = "Failure", message = "Wrong username or password!")

tk.Label(root, text = "Username:").pack(pady = "20px")
usernameField = tk.Entry(root)
usernameField.pack(pady = "5px")
tk.Label(root, text = "Password:").pack(pady = "20px")
passwordField = tk.Entry(root, show = "*")
passwordField.pack(pady = "5px")
loginButton = tk.Button(root, text = "submit", command = submitLogin).pack()
root.mainloop()
