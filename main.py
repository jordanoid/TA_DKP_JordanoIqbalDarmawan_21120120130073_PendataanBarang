from credentials import credential
from screen import *

def login():
    username = unameentry.get()
    password = passentry.get()

    user = credential(username, password)
    log = user.check()
    if log:
        messagebox.showinfo("", "Login berhasil")
        homescreen()
    else:
        messagebox.showinfo("", "Login gagal")

root = Tk()

root.geometry("300x250")
root.title("Pendataan Barang")
Label(root, text="").pack()
frame = Frame(root, bg = "#3bb9eb", bd = 5 )
frame.pack()
label1 = Label(frame, text = "Masukkan username dan password", bg = "#3bb9eb")
label1.pack(side = "top")
Label(frame, text="", bg = "#3bb9eb").pack()
label2 = Label(frame, text = "username :", bg = "#3bb9eb")
label2.pack()
unameentry = Entry(frame)
unameentry.pack()
label3 = Label(frame, text = "password :", bg = "#3bb9eb")
label3.pack()
passentry = Entry(frame)
passentry.pack()
Label(frame, text="", bg = "#3bb9eb").pack()
login_image = PhotoImage(file = 'images/login_button.png')
login_button = Button(root, image = login_image , command = login, borderwidth = 0)
login_button.pack()

root.mainloop()