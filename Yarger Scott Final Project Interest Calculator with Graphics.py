#SDEV 140 class, Spring 2023, Scott Yarger Final Project Part 2

# import tkinter
from tkinter import *
 
# Function for clearing the contents of all entry boxes  
def clear_all() :
 
    # content of entry boxes deleted
    principal_field.delete(0, END)  
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
   
    # set focus on the principal_field entry box 
    principal_field.focus_set()
 
 
# Function to find compound interest 
def calculate_ci():
 
    # get a content from entry box
    principal = int(principal_field.get())
 
    rate = float(rate_field.get())
 
    time = int(time_field.get())
     
    # Calculates compound interest 
    CI = principal * (pow((1 + rate / 100), time))
 
    # insert method for value in the text entry box.
    compound_field.insert(10, CI)
 
 
# Driver code
if __name__ == "__main__" :
   
    # Create a GUI window
    root = Tk()
   
    # Set the background color of GUI window
    root.configure(background = 'light green')
   
    # Set the configuration dimensions of GUI window
    root.geometry("400x250")
   
    # set the name of tkinter GUI window
    root.title("Compound Interest Calculator") 
       
    # Create a Principal Amount : label
    label1 = Label(root, text = "Principal Amount(PA) : ",
                   fg = 'black', bg = 'light blue')
   
    # Create a Rate : label
    label2 = Label(root, text = "Rate(%) : ",
                   fg = 'black', bg = 'light blue')
       
    # Create a Time : label
    label3 = Label(root, text = "Time(years) : ",
                   fg = 'black', bg = 'light blue')
 
    # Create a Compound Interest : label
    label4 = Label(root, text = "Compound Interest : ",
                   fg = 'black', bg = 'light blue')
 
    # grid method is used for placing 
    # in table structure.
 
    # padx keyword argument used to set padding along x-axis.
    # pady keyword argument used to set padding along y-axis.
    label1.grid(row = 1, column = 0, padx = 10, pady = 10) 
    label2.grid(row = 2, column = 0, padx = 10, pady = 10) 
    label3.grid(row = 3, column = 0, padx = 10, pady = 10)
    label4.grid(row = 5, column = 0, padx = 10, pady = 10)
 
    # Create entry boxes 
    principal_field = Entry(root)
    rate_field = Entry(root) 
    time_field = Entry(root)
    compound_field = Entry(root)
 
    # grid method padx x-axis pady along y-axis .
    principal_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
    rate_field.grid(row = 2, column = 1, padx = 10, pady = 10) 
    time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
    compound_field.grid(row = 5, column = 1, padx = 10, pady = 10)
 
    # Create a Submit Button to calculate_compound function 
    button1 = Button(root, text = "Submit", bg = "light blue", 
                     fg = "black", command = calculate_ci)
   
    # Create a Clear Button and attached to clear_all function 
    button2 = Button(root, text = "Clear", bg = "light blue", 
                     fg = "black", command = clear_all)
   
    button1.grid(row = 4, column = 1, pady = 10)
    button2.grid(row = 6, column = 1, pady = 10)
 # Reset from tkinter import * for second window.
# Conflict occurs between grid and pack() if kept in same window

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title ('Scott First window')
# First window image calling results in multiple PIL instances error
#first_img = ImageTk.PhotoImage(Image.open("c:/png/House.png").resize((80,80), Image.LANCZOS))
#first_label = Label(root, image=first_img).pack()

def open():
    global my_img
    top=Toplevel()
    top.title ('Scott Second window')
    my_img = ImageTk.PhotoImage(Image.open("Bank.png").resize((80,80), Image.LANCZOS))
    my_label = Label(top, image=my_img).pack()
    
btn=Button(root, text="Open Second Window", command=open).pack()

def open2():
    global my_img2
    top2=Toplevel()
    top2.title ('Scott Third window')
    my_img2 = ImageTk.PhotoImage(Image.open("House.png").resize((80,80), Image.LANCZOS))
    my_label2 = Label(top2, image=my_img2).pack()

btn3=Button(root, text="Open Third Window", command=open2).pack()

# Start program
root.mainloop()
