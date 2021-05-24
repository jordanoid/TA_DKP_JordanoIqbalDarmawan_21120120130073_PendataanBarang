from tkinter import *
from tkinter import messagebox

def homescreen():
    screen1 = Toplevel()
    screen1.geometry("800x600")
    frame = Frame(screen1, bg = "#3bb9eb", bd = 5 )
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
    