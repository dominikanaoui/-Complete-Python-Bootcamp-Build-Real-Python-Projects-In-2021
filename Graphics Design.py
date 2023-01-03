from tkinter import *

root=Tk()
root.title('Graphics')

canvas=Canvas(width=300,height=150)
canvas.pack()

redline=canvas.create_line(0,0,300,50,fill='red')
blueline=canvas.create_line(0,150,300,50,fill='blue')
yellowbox=canvas.create_rectangle(50,50,150,70,fill='yellow')

#canvas.delete(blueline)
#canvas.delete(ALL)

root.mainloop()