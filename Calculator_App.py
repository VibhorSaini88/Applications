#Import Module:->
import tkinter
from tkinter import *
from tkinter import ttk
import math

#create function:->
def dlt():
    entry.delete(len(entry.get()) - 1)
def clear():
    entry.delete(0,END)
def seven():
    entry.insert(END,7)

def eight():
    entry.insert(END,8)

def nine():
    pass
def slash():
    pass
def four():
    pass
def five():
    pass
def six():
    pass
def multi():
    entry.insert(END,"*")
def one():
    pass
def two():
    pass
def three():
    pass
def minus():
    pass
def dot():
    pass
def zero():
    pass
def equal():
    pass
def plus():
    pass

#Create Window:->
root = Tk()

#Window Design:->
root.title("calculator")
root.geometry('224x300')
root.resizable(TRUE,FALSE)

#Entry Box:->
entry = Entry(root,width=33,bd=6,bg='#0EDFD0')
entry.grid(row=0,column=0,padx=8,pady=10)

#Create Label:->
lbl1 = Label(root,width=21,height=2,bg='gray').place(x=9,y=37)

#Create Buttons:->
btn = Button(root,text='DEL',bg='red',activebackground='black',activeforeground='white',fg='white',bd=6,command=dlt).place(x=9,y=37)
btn1 = Button(root,text='CLEAR',bg='black',activebackground='black',activeforeground='white',fg='white',bd=6,command=clear).place(x=162,y=37)
btn2 = Button(root,text='7',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=seven).place(x=9,y=70)
btn3 = Button(root,text='8',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=eight).place(x=60,y=70)
btn4 = Button(root,text='9',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=nine).place(x=110,y=70)
btn5 = Button(root,text='/',bg='#CC0EDF',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=slash).place(x=162,y=70)
btn6 = Button(root,text='4',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=four).place(x=9,y=119)
btn7 = Button(root,text='5',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=five).place(x=60,y=119)
btn8 = Button(root,text='6',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=six).place(x=110,y=119)
btn9 = Button(root,text='x',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=multi).place(x=162,y=119)
btn10 = Button(root,text='1',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=one).place(x=9,y=168)
btn11 = Button(root,text='2',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=two).place(x=60,y=168)
btn12 = Button(root,text='3',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=three).place(x=110,y=168)
btn13 = Button(root,text='-',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=minus).place(x=162,y=168)
btn14 = Button(root,text='.',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=dot).place(x=9,y=218)
btn15 = Button(root,text='0',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=zero).place(x=60,y=218)
btn16 = Button(root,text='=',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=equal).place(x=110,y=218)
btn17 = Button(root,text='+',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=plus).place(x=162,y=218)


#Output Terminator:->
root.mainloop()