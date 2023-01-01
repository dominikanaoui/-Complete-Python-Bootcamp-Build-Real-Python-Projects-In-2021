from tkinter import *

root=Tk()
def pro():
    r=v.get()
    if r == 1:
        mylabel1 = Label(text='  Java programming  ').pack()
    elif r == 2:
        mylabel2 = Label(text='  Python programming  ').pack()
    elif r == 3:
        mylabel3 = Label(text='  PHP programming  ').pack()
    else:
        mylabel4 = Label(text='  Ruby programming  ').pack()

root.title('Radio Button')
root.geometry('300x400')

v=IntVar()
v.set(2)

Radios = [('Java',1),('Python',2),('PHP',3),('Ruby',4)]

mylabel=Label(text='Computer Programming').pack()

for rad, val in Radios:
    Radiobutton(text=rad,padx=10,variable=v,value=val,command=pro, indicatoron=0, width=50).pack(anchor=W)

'''
Radiobutton(text='radio1').pack(anchor=W)
Radiobutton(text='radio2').pack(anchor=W)
'''

'''
Radiobutton(text='Java', padx=10, variable=v, value=1, command=pro).pack(anchor=W)
Radiobutton(text='Python', padx=10,variable=v, value=2, command=pro).pack(anchor=W)
Radiobutton(text='PHP', padx=10, variable=v, value=3, command=pro).pack(anchor=W)
Radiobutton(text='Ruby', padx=10, variable=v, value=4, command=pro).pack(anchor=W)
'''

root.mainloop()