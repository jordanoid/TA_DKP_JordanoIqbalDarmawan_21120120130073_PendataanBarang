from tkinter import *
from tkinter import messagebox
from credentials import credential

def login():
    username = unameentry.get()
    password = passentry.get()

    user = credential(username, password)
    log = user.check()
    if log:
        messagebox.showinfo("", "Login berhasil")
    else:
        messagebox.showinfo("", "Login gagal")

root = Tk()

root.geometry("300x250")
root.title("Login")
Label(text="").pack()
label1 = Label(root, text = "Masukkan username dan password untuk login")
label1.pack(side = "top")
Label(text="").pack()
label2 = Label(root, text = "username :")
label2.pack()
unameentry = Entry(root)
unameentry.pack()
label3 = Label(root, text = "password :")
label3.pack()
passentry = Entry(root)
passentry.pack()
Label(text="").pack()
login_button = Button(root, text = "Login", command = login)
login_button.pack()

root.mainloop()