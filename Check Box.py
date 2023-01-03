from tkinter import *

def check():
    #print(chkb1.get(),chkb2.get(),chkb3.get(),chkb4.get())
    r1=chkb1.get()
    r2=chkb2.get()
    r3=chkb3.get()
    r4=chkb4.get()

    if r1 == 1:
        Label(text='   Java Programming   ').pack()
    if r2 == 1:
        Label(text='   Python Programming   ').pack()
    if r3 == 1:
        Label(text='   PHP Programming   ').pack()
    if r4 == 1:
        Label(text='   Ruby Programming   ').pack()

root=Tk()
root.geometry('300x400')
root.title('CheckBox')

chkb1 = IntVar()
Checkbutton(text='Java',variable=chkb1).pack(anchor=W)
chkb2 = IntVar()
Checkbutton(text='Python',variable=chkb2).pack(anchor=W)
chkb3 = IntVar()
Checkbutton(text='PHP',variable=chkb3).pack(anchor=W)
chkb4 = IntVar()
Checkbutton(text='Ruby',variable=chkb4).pack(anchor=W)

btn1=Button(text='Get Value', command=check).pack(anchor=W)
btn2=Button(text='Close', command=root.destroy).pack(anchor=W)

'''
chkb1 = IntVar()
Checkbutton(text='Java',variable=chkb1).grid(row=0,sticky=W)
chkb2 = IntVar()
Checkbutton(text='Python',variable=chkb2).grid(row=1,sticky=W)
chkb3 = IntVar()
Checkbutton(text='PHP',variable=chkb3).grid(row=2,sticky=W)
chkb4 = IntVar()
Checkbutton(text='Ruby',variable=chkb4).grid(row=3,sticky=W)

btn1=Button(text='Get Values', command=check).grid(row=4, sticky=W)
btn2=Button(text='Close', command=root.destroy).grid(row=5, sticky=E)
'''

root.mainloop()
