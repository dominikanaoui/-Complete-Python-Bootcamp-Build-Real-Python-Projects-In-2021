from tkinter import *
from tkinter import ttk

def click():
    Label(text='   Your favorite fruit is: '+var.get(), font=10).grid(row=2,column=1)

root=Tk()
root.title('Combo Box')

var=StringVar(value="Choose a fruit")
combo=ttk.Combobox(width=25,textvariable=var,font=10)
combo['values']=('Apple','Orange','Mango','Cashew','Papaya','Melon')
combo.grid(row=0,column=1)

ttk.Label(text='Select your favorite fruit: ',font=10).grid(row=0,column=0)

btn=ttk.Button(text='Click me!', command=click)
btn.grid(row=1, column=2)

root.mainloop()