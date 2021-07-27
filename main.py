from credentials import *
from screen import *

def main():
    def login():
        global username
        global password
        username = unameentry.get()
        password = passentry.get()
        user = credential(username, password)
        log = user.check()
        if log:
            messagebox.showinfo("", "Login berhasil")
            homescreen()

        else:
            messagebox.showinfo("", "Login gagal")
        unameentry.delete(0, END)
        passentry.delete(0, END)

    root = Tk()

    root.geometry("300x250")
    root.resizable(0,0)
    root.title("Pendataan Barang")
    Label(root, text="").pack()
    frame = Frame(root, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
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
    login_button = Button(frame, image = login_image , command = login, borderwidth = 5, bg = "#3bb9eb")
    login_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()