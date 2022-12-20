from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry('550x500+100+200')

def mycolour():
    colour = askcolor()
    mylabel = Label (text="That's your preferred colour", bg=colour[1]).pack()
    print(colour)

button1 = Button(text='Please, choose colour', command=mycolour).pack()

root.mainloop()