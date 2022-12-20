from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('1000x500+200+200')
root.title('File opener')
#it lets us to select a file and gives us direction to file
#it will read only .txt files

def filedialog():
    fileopen = askopenfilename()
    fileread = fileopen
    file = open(fileread)
    mylabel = Label(text=file.read(), font=10).pack()

button1 = Button(text='Open file', width = 50, command=filedialog).pack()

root.mainloop()