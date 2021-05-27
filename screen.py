from tkinter import *
from tkinter import messagebox, ttk
from credentials import changeCredential

data = {"bangku" : 10,
        "meja" : 10,
        "papan tulis" : 2,
        "spidol" : 3,
        "pensil" : 20,
        "penghapus" : 20,
        "tinta spidol" : 4,
        "sapu" : 2,
        "pel" : 2,
        "pengki" : 2,
        "taplak meja" : 2
        }

def testButton():
    messagebox.showinfo("", "Button Active")

def homescreen():
    global stg_image
    global list_image
    global edit_image
    global exit_image
    global screen1
    screen1 = Toplevel()
    screen1.geometry("400x300")
    screen1.resizable(0,0)
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
    edit_button = Button(frame, image = edit_image, borderwidth = 5, command = editscreen, bg = "#3bb9eb")
    edit_button.place(relx = 0.39, rely = 0.3)
    edit_label = Label(frame, text = "Ubah Daftar", bg = "#3bb9eb")
    edit_label.place(relx = 0.4, rely = 0.65)

    def exit():
        screen1.destroy()

    exit_image = PhotoImage(file = "images/exit_button.png")
    exit_button = Button(frame, image = exit_image, borderwidth = 5, command = exit, bg = "#3bb9eb")
    exit_button.place(relx = 0.48, rely = 0.9)

def setscreen():
    screen1.destroy()
    screen2 = Toplevel()
    screen2.resizable(0,0)
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
    ok_button = Button(frame, text = "OK", bg = "#3bb9eb", borderwidth = 5, command = ok)
    ok_button.pack()
    def back():
        screen2.destroy()
        homescreen()
    back_button = Button(screen2, text = "Back", borderwidth = 5, command = back)
    back_button.pack(side = BOTTOM)

def listscreen():
    screen1.destroy()
    screen3 = Toplevel()
    screen3.geometry("250x350")
    screen3.resizable(0,0)
    frame = Frame(screen3, bg = "#3bb9eb", bd = 5 )
    frame.pack(pady = 20)

    #sistem tabel (new)

    tree_scroll = Scrollbar(frame)
    tree_scroll.pack(side = RIGHT, fill = Y)

    table = ttk.Treeview(frame, yscrollcommand = tree_scroll.set)

    tree_scroll.config(command = table.yview)

    table['columns'] = ("Nama Barang", "Jumlah")
    table.column("#0", width = 0, stretch = NO)
    table.column("Nama Barang", width = 120, anchor = W)
    table.column("Jumlah", width = 80, anchor = CENTER)

    table.heading("Nama Barang", text = "Nama Barang", anchor = W)
    table.heading("Jumlah", text = "Jumlah", anchor = CENTER)

    counter = 0
    for i in data:
        table.insert(parent = "", index = 'end', iid = counter, text = "", values = (i, data[i]))
        counter += 1

    table.pack()

    #sitem tabel (old)

    # label1 = Label(frame, text = "Nama barang", bg = "#3bb9eb", justify = LEFT, anchor = "w", width = 15)
    # label1.grid(column = 0, row = 0)
    # label2 = Label(frame, text = "Jumlah", bg = "#3bb9eb")
    # label2.grid(column = 2, row = 0)
    # counter = 1
    # for i in data:
    #     Label(frame, text = i, bg = "#3bb9eb", justify = LEFT, anchor = "w", width = 15).grid(column = 0, row = counter, sticky = W)
    #     Label(frame, text = data[i], bg = "#3bb9eb").grid(column = 2, row = counter)
    #     counter += 1

    def back():
        screen3.destroy()
        homescreen()
    back_button = Button(screen3, text = "Back", borderwidth = 5, command = back)
    back_button.pack()

def editscreen():

    def add():
        try:
            nama = str(barang.get())
            qty = int(jumlah.get())
            if nama and qty != "":
                if nama in data:
                    messagebox.showinfo("Error!", "Barang sudah ada! Gunakan tombol Ubah!")
                else:
                    data[nama] = qty
                    messagebox.showinfo("Success!", "Data barang berhasil ditambahkan!")
            else:
                messagebox.showinfo("Error!", "Isi kotak nama!")
        except:
            messagebox.showinfo("Error!", "Isi kotak jumlah dengan angka!")


    def change():
        try:
            nama = str(barang.get())
            qty = int(jumlah.get())
            if nama and qty != "":
                if nama not in data:
                    messagebox.showinfo("Error!", "Barang tidak ada! Gunakan tombol Tambah!")
                else:
                    data[nama] = qty
                    messagebox.showinfo("Success!", "Data barang berhasil diubah!")
            else:
                messagebox.showinfo("Error!", "Isi kotak dengan benar!")
        except:
            messagebox.showinfo("Error!", "Isi kotak jumlah dengan angka!")

    def delete():
        nama = str(barang2.get())
        if nama != "":
            if nama not in data:
                messagebox.showinfo("Error!", "Barang tidak ada! Masukan nama dengan benar!")
            else:
                del data[nama]
        else:
            messagebox.showinfo("Error!", "Isi kotak dengan benar!") 

    screen1.destroy()
    screen4 = Toplevel()
    screen4.geometry("400x300")
    frame = Frame(screen4, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

    Label(frame, text = "Tambah/Ubah").grid(column = 0, row = 0, sticky = W)
    label1 = Label(frame, text = "Nama barang", bg = "#3bb9eb", justify = LEFT, anchor = "w", width = 15)
    label1.grid(column = 0, row = 1, sticky = W)
    barang = Entry(frame)
    barang.grid(column = 0, row = 2)

    Label(frame, text="     ", bg = "#3bb9eb").grid(column = 1, row = 0)

    label2 = Label(frame, text = "Jumlah", bg = "#3bb9eb", justify = LEFT, anchor = "w", width = 15)
    label2.grid(column = 2, row = 1, sticky = W)
    jumlah = Entry(frame)
    jumlah.grid(column = 2, row = 2)

    add_button = Button(screen4, text = "Tambah", bg = "#3bb9eb", borderwidth = 5, command = add)
    add_button.place(relx = 0.12, rely = 0.35)

    change_button = Button(screen4, text = "Ubah", bg = "#3bb9eb", borderwidth = 5, command = change)
    change_button.place(relx = 0.3, rely = 0.35)

    Label(frame, text="", bg = "#3bb9eb").grid(column = 0, row = 3)
    Label(frame, text="", bg = "#3bb9eb").grid(column = 0, row = 4)
    Label(frame, text="", bg = "#3bb9eb").grid(column = 0, row = 5)
    Label(frame, text= "Hapus").grid(column = 0, row = 6, sticky = W)

    label3 = Label(frame, text = "Nama barang", bg = "#3bb9eb", justify = LEFT, anchor = "w", width = 15)
    label3.grid(column = 0, row = 7, sticky = W)

    barang2 = Entry(frame)
    barang2.grid(column = 0, row = 8)

    Label(frame, text="", bg = "#3bb9eb").grid(column = 0, row = 9)

    delete_button = Button(screen4, text = "Hapus", bg = "#3bb9eb", borderwidth = 5, command = delete)
    delete_button.place(relx = 0.12, rely = 0.78)

    def back():
        screen4.destroy()
        homescreen()
    back_button = Button(screen4, text = "Back", borderwidth = 5, command = back)
    back_button.pack(side = BOTTOM)
