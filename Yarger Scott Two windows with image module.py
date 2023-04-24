#SDEV 140 class, Spring 2023, Scott Yarger Final Project Images Module
from tkinter import *
from PIL import ImageTk,Image
#import customtkinter

root = Tk()
root.title ('Scott First window')
first_img = ImageTk.PhotoImage(Image.open("House.png").resize((80,80), Image.LANCZOS))
first_label = Label(root, image=first_img).pack()

def open():
    global my_img
    top=Toplevel()
    top.title ('Scott Second window')
    my_img = ImageTk.PhotoImage(Image.open("Bank.png").resize((80,80), Image.LANCZOS))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top,text="close window", command=top.destroy).pack()

btn=Button(root, text="Open Second Window", command=open).pack()

mainloop()
