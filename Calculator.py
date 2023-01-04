#we import all what is in library tkinter
from tkinter import *

#we define functions
def btn(numbers):
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator=''
    txt_input.set('')

def Equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator=''

#we import first library called Tk, we create a window
root=Tk()
root.title('Calculator')
root.geometry('+400+10')

operator=''
txt_input=StringVar(value='Start calculating...')

#======================================we create a SCREEN======================================
Display=Entry(root,font=('arial',30,'bold'),
              fg='black',bg='green',justify='right',bd=60,textvariable=txt_input).grid(columnspan=4)

#======================================we create ROW 1======================================
btn7=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='7',fg='black',bd=8, command=lambda: btn(7)).grid(row=1,column=0)
btn8=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='8',fg='black',bd=8, command=lambda: btn(8)).grid(row=1,column=1)
btn9=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='9',fg='black',bd=8, command=lambda: btn(9)).grid(row=1,column=2)
btnPlus=Button(root,padx=80,pady=15,font=('arial',30,'bold'),
                bg='orange', text='+',fg='black',bd=8, command=lambda: btn('+')).grid(row=1,column=3)

#======================================we create ROW 2======================================
btn4=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='4',fg='black',bd=8, command=lambda: btn(4)).grid(row=2,column=0)
btn5=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='5',fg='black',bd=8, command=lambda: btn(5)).grid(row=2,column=1)
btn6=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='6',fg='black',bd=8, command=lambda: btn(6)).grid(row=2,column=2)
btnMinus=Button(root,padx=85,pady=15,font=('arial',30,'bold'),
                bg='orange', text='-',fg='black',bd=8, command=lambda: btn('-')).grid(row=2,column=3)

#======================================we create ROW 3======================================
btn1=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='1',fg='black',bd=8, command=lambda: btn(1)).grid(row=3,column=0)
btn2=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='2',fg='black',bd=8, command=lambda: btn(2)).grid(row=3,column=1)
btn3=Button(root,padx=30,pady=15,font=('arial',30,'bold'),
            bg='white', text='3',fg='black',bd=8, command=lambda: btn(3)).grid(row=3,column=2)
btnMultiply=Button(root,padx=85,pady=15,font=('arial',30,'bold'),
                bg='orange', text='*',fg='black',bd=8, command=lambda: btn('*')).grid(row=3,column=3)

#======================================we create ROW 4======================================
btnOpenBracket = Button(root, padx=35, pady=15, font=('arial', 30, 'bold'),
                        bg='green', text='(', fg='black', bd=8, command=lambda: btn('(')).grid(row=4, column=0)
btn0=Button(root,padx=35,pady=15,font=('arial',30,'bold'),
            bg='white', text='0',fg='black',bd=8, command=lambda: btn(0)).grid(row=4,column=1)
btnCloseBracket = Button(root, padx=35, pady=15, font=('arial', 30, 'bold'),
                         bg='green', text=')', fg='black', bd=8, command=lambda: btn(')')).grid(row=4, column=2)
btnDivision=Button(root,padx=85,pady=15,font=('arial',30,'bold'),
            bg='orange', text='/',fg='black',bd=8, command=lambda: btn('/')).grid(row=4,column=3)

#======================================we create ROW 5======================================
btnEquals=Button(root,padx=100,pady=15,font=('arial',30,'bold'),
            bg='red', text='=',fg='black',bd=8, command=Equal).grid(row=5,column=0, columnspan=2)
btndDot = Button(root, padx=35, pady=15, font=('arial', 30, 'bold'),
                bg='green', text='.', fg='black', bd=8, command=lambda: btn('.')).grid(row=5, column=2)
btnClear=Button(root,padx=40,pady=15,font=('arial',30,'bold'),
                bg='red', text='Clear',fg='black',bd=8, command=Clear).grid(row=5,column=3)

#it makes window visible
root.mainloop()