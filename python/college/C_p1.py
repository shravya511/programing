from tkinter import *
expr=""
def press(num):
    global expr
    expr=expr+str(num)
    equation.set(expr)
def equalpress():
    try:
        global expr
        total=str(eval(expr))
        equation.set(total)
        expr=""
    except:
        equation.set("Error")
        expr=""
def clear():
    global expr
    expr=""
    equation.set("")
gui=Tk()
gui.configure(background="light green")
gui.title("Simple Calculator")
gui.geometry("400x250")
equation=StringVar()
expr_field=Entry(gui,textvariable=equation)
expr_field.grid(columnspan=4,ipadx=70)
b1=Button(gui,text='1',command=lambda:press(1),height=2,width=7)
b1.grid(row=2,column=0)
b2=Button(gui,text='2',command=lambda:press(2),height=2,width=7)
b2.grid(row=2,column=1)
b3=Button(gui,text='3',command=lambda:press(3),height=2,width=7)
b3.grid(row=2,column=2)
b4=Button(gui,text='4',command=lambda:press(4),height=2,width=7)
b4.grid(row=3,column=0)
b5=Button(gui,text='5',command=lambda:press(5),height=2,width=7)
b5.grid(row=3,column=1)
b6=Button(gui,text='6',command=lambda:press(6),height=2,width=7)
b6.grid(row=3,column=2)
b7=Button(gui,text='7',fg='black',command=lambda:press(7),height=2,width=7)
b7.grid(row=4,column=0)
b8=Button(gui,text='8',command=lambda:press(8),height=2,width=7)
b8.grid(row=4,column=1)
b9=Button(gui,text='9',command=lambda:press(9),height=2,width=7)
b9.grid(row=4,column=2)
b0=Button(gui,text='0',command=lambda:press(0),height=2,width=7)
b0.grid(row=5,column=0)
plus=Button(gui,text='+',command=lambda:press("+"),height=2,width=7)
plus.grid(row=2,column=3)
minus=Button(gui,text='-',command=lambda:press("-"),height=2,width=7)
minus.grid(row=3,column=3)
mul=Button(gui,text='x',command=lambda:press("*"),height=2,width=7)
mul.grid(row=4,column=3)
div=Button(gui,text='/',command=lambda:press("/"),height=2,width=7)
div.grid(row=5,column=3)
equal=Button(gui,text='=',command=equalpress,height=2,width=7)
equal.grid(row=5,column=2)
clear=Button(gui,text='Clear',command=clear,height=2,width=7)
clear.grid(row=5,column=1)
dec=Button(gui,text='.',command=lambda:press("."),height=2,width=7)
dec.grid(row=6,column=0)
gui.mainloop()