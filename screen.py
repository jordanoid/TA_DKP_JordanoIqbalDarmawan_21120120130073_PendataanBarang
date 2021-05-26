from tkinter import *
from tkinter import messagebox
from credentials import changeCredential

def testButton():
    messagebox.showinfo("", "Button Active")

def homescreen():
    global stg_image
    global list_image
    global edit_image
    global screen1
    screen1 = Toplevel()
    screen1.geometry("400x300")
    frame = Frame(screen1, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
    test = Label(screen1 , text = "Halaman Utama", bg = "#3bb9eb")
    test.pack(pady = 20)

    stg_image = PhotoImage(file = "images/setting_button.png")
    stg_button = Button(frame, image = stg_image, borderwidth = 5, command = setscreen, bg = "#3bb9eb")
    stg_button.place(relx = 0.68, rely = 0.3)
    stg_label = Label(frame, text = "Set Account", bg = "#3bb9eb")
    stg_label.place(relx = 0.69, rely = 0.65)

    list_image = PhotoImage(file = "images/list_button.png")
    list_button = Button(frame, image = list_image, borderwidth = 5, command = listscreen, bg = "#3bb9eb")
    list_button.place(relx = 0.09, rely = 0.3)
    list_label = Label(frame, text = "Daftar Barang", bg = "#3bb9eb")
    list_label.place(relx = 0.085, rely = 0.65)

    edit_image = PhotoImage(file = "images/edit_button.png")
    edit_button = Button(frame, image = edit_image, borderwidth = 5, command = testButton, bg = "#3bb9eb")
    edit_button.place(relx = 0.39, rely = 0.3)
    edit_label = Label(frame, text = "Ubah Daftar", bg = "#3bb9eb")
    edit_label.place(relx = 0.4, rely = 0.65)

def setscreen():
    global screen2
    screen1.destroy()
    screen2 = Toplevel()
    screen2.geometry("300x250")
    frame = Frame(screen2, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

    label1 = Label(frame, text = "username baru :", bg = "#3bb9eb")
    label1.pack()
    uname = Entry(frame)
    uname.pack()

    label2 = Label(frame, text = "password baru :", bg = "#3bb9eb")
    label2.pack()
    pw = Entry(frame)
    pw.pack()
    Label(frame, text="", bg = "#3bb9eb").pack()
    
    def ok():
        newUname = uname.get()
        newPass = pw.get()
        changeCredential(newUname, newPass)
        screen2.destroy()
        homescreen()
    ok_button = Button(frame, text = "OK", bg = "#3bb9eb", command = ok)
    ok_button.pack()

def listscreen():
    def ok():
        screen3.destroy()
        homescreen()
    global data
    screen1.destroy()
    data = {"bangku" : 10, "meja" : 10, "papan tulis" : 2, "spidol" : 3}
    screen3 = Toplevel()
    frame = Frame(screen3, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
    label1 = Label(frame, text = "Nama barang", bg = "#3bb9eb")
    label1.grid(column = 0, row = 0)
    label2 = Label(frame, text = "Jumlah", bg = "#3bb9eb")
    label2.grid(column = 2, row = 0)
    counter = 1
    for i in data:
        Label(frame, text = i, bg = "#3bb9eb").grid(column = 0, row = counter)
        Label(frame, text = data[i], bg = "#3bb9eb").grid(column = 2, row = counter)
        counter += 1
    ok_button = Button(screen3, text = "Back", bg = "#3bb9eb", command = ok)
    ok_button.place(relx = 0.7, rely = 0.7)