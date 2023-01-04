from tkinter import *

root = Tk()
root.title('Image')
#root.geometry('300x400')

photo = PhotoImage(file='Face.gif')
mylabel = Label(root, image = photo)
mylabel.pack()

root.mainloop()