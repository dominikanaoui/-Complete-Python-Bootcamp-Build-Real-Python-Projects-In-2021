from tkinter import *
from tkinter import ttk

def convert():
    var2=indicator.get()
    var3=var1.get()
    if var2=='China':
        e3.delete(0, END)
        var4=((var3*6.91),'Chinese Yuan') #values in the day of 3rd Jan 2023
        e3.insert(0,var4)
    elif var2=='France':
        e3.delete(0, END)
        var4=((var3*0.95),'Euro')
        e3.insert(0,var4)
    elif var2 == 'Ghana':
        e3.delete(0, END)
        var4 = ((var3 * 10.01), 'Ghanaian Cedi')
        e3.insert(0, var4)
    elif var2 == 'Mexico':
        e3.delete(0, END)
        var4 = ((var3 * 19.51), 'Mexican Peso')
        e3.insert(0, var4)
    elif var2 == 'Nigeria':
        e3.delete(0, END)
        var4 = ((var3 * 448.08), 'Nigerian Naira')
        e3.insert(0, var4)
    elif var2 == 'USA':
        e3.delete(0, END)
        var4 = ((var3 * 1.00), 'US Dollars')
        e3.insert(0, var4)
    else:
        e3.delete(0, END)
        var4=('ERROR: Please, choose a country!')
        e3.insert(0,var4)

def clear():
    e1.delete(0, END)
    e3.delete(0, END)

root=Tk()
root.title('Currency Converter')

var1=IntVar()

indicator=StringVar(value='Choose a country')

Label(text='Currency Converter', padx=10, font=('arial', 30, 'bold')).grid(row=0, column=1)

Label(text='Amount ($)', padx=10, font=('arial', 30, 'bold')).grid(row=1, sticky=W)
e1=Entry(width=30, font=('arial', 30, 'bold'), textvariable=var1)
e1.grid(row=1, column=1)

Label(text='Country', padx=10, font=('arial', 30, 'bold')).grid(row=2, sticky=W)
e2=ttk.Combobox(width=29, font=('arial', 30, 'bold'),textvariable=indicator)
e2['values']=('China','France','Ghana','Mexico','Nigeria','USA')
e2.grid(row=2, column=1)

Label(text='Total', padx=10, font=('arial', 30, 'bold')).grid(row=3, sticky=W)
e3=Entry(width=30, font=('arial', 30, 'bold'))
e3.grid(row=3, column=1)

Button(text='Convert', padx=10, font=('arial', 30, 'bold'), width=15, command=convert).grid(row=4, column=1, sticky=W)
Button(text='Clear', padx=10, font=('arial', 30, 'bold'), width=15, command=clear).grid(row=4, column=1, sticky=E)

root.mainloop()