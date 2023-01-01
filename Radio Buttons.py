from tkinter import *

root=Tk()
def pro():
    r=v.get()
    if r == 1:
        mylabel1 = Label(text='  Java programming  ').grid(row=2, column=0)
    elif r == 2:
        mylabel2 = Label(text='  Python programming  ').grid(row=2, column=0)
    elif r == 3:
        mylabel3 = Label(text='  PHP programming  ').grid(row=2, column=0)
    else:
        mylabel4 = Label(text='  Ruby programming  ').grid(row=2, column=0)

root.title('Radio Button')
root.geometry('450x300')

v=IntVar()
v.set(2)

#mylabel=Label(text='Computer Programming').pack()
mylabel=Label(text='Computer Programming').grid(row=0, column=2)

Radiobutton(text='Java', padx=10, pady=30, variable=v, value=1, command=pro).grid(row=1, column=0)
Radiobutton(text='Python', padx=10, pady=30, variable=v, value=2, command=pro).grid(row=1, column=1)
Radiobutton(text='PHP', padx=10, pady=30, variable=v, value=3, command=pro).grid(row=1, column=2)
Radiobutton(text='Ruby', padx=10, pady=30, variable=v, value=4, command=pro).grid(row=1, column=3)

root.mainloop()