from tkinter import *

counter = 0
def digit_counter(mylabel):
    counter = 0
    def digit():
        global counter
        counter += 1
        mylabel.config(text=str(counter))
        mylabel.after(1000, digit)
    digit()

root = Tk()

root.title('Digit counter')
mylabel = Label(fg='red', font=100)
mylabel.pack()
digit_counter(mylabel)
btn = Button(text='Terminate', width=50, command=root.destroy)
btn.pack()
root.mainloop()