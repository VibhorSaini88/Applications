#Import Modules:->
import tkinter
from tkinter import *
from tkinter import ttk
import math

class calc:					#Root class:->
    def operations(self):

    def clear(self):
        self.entry.delete(len(self.entry.get()) - 1)
    def clearall(self):
        self.entry.delete(0,END)
    def action(self,num):
        self.entry.insert(END,num)
    def equals(self):
        self.entry.delete(0,END)

        entry.insert(1,result.get())


    def elements(self,root):              #initial call method:->
        root.title("calculator")
        root.geometry('224x300')
        root.resizable(TRUE,FALSE)

        self.entry = Entry(root,width=33,bd=6,bg='#0EDFD0')         #Entry Box:->
        self.entry.grid(row=0,column=0,padx=8,pady=10)

        self.lbl1 = Label(root,width=21,height=2,bg='gray').place(x=9,y=37)      #Create Label:->

                                    #Create Buttons:->
        Button(root,text='DEL',bg='red',activebackground='black',activeforeground='white',fg='white',bd=6,command=lambda:self.clear()).place(x=9,y=37)
        Button(root,text='CLEAR',bg='black',activebackground='black',activeforeground='white',fg='white',bd=6,command=lambda:self.clearall()).place(x=162,y=37)
        Button(root,text='7',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(7)).place(x=9,y=70)
        Button(root,text='8',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(8)).place(x=60,y=70)
        Button(root,text='9',bg='#0A3EE0',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(9)).place(x=110,y=70)
        Button(root,text='/',bg='#CC0EDF',activebackground='pink',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action('/')).place(x=162,y=70)
        Button(root,text='4',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(4)).place(x=9,y=119)
        Button(root,text='5',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(5)).place(x=60,y=119)
        Button(root,text='6',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(6)).place(x=110,y=119)
        Button(root,text='x',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action('*')).place(x=162,y=119)
        Button(root,text='1',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(1)).place(x=9,y=168)
        Button(root,text='2',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(2)).place(x=60,y=168)
        Button(root,text='3',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(3)).place(x=110,y=168)
        Button(root,text='-',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action('-')).place(x=162,y=168)
        Button(root,text='.',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action('.')).place(x=9,y=218)
        Button(root,text='0',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action(0)).place(x=60,y=218)
        Button(root,text='=',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.equals()).place(x=110,y=218)
        Button(root,text='+',bg='#0A3EE0',activebackground='#14D442',activeforeground='black',fg='white',width=5,height=2,bd=6,command=lambda:self.action('+')).place(x=162,y=218)

#main():->
window = Tk()           #create gui window.
obj=calc()              #object created of class name calc.
obj.elements(window)

window.mainloop()       #terminated loop.