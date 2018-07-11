#Import Modules:->
import tkinter
from tkinter import *
import random

#create global list of task:->
task = ["go to gym","complete Project","go to market","walking in the Evening","Book reading","going for milk","seeing movie"]

#create functions:->
def add():
    list_box.insert(END,entry_box.get())
    entry_box.delete(0,END)
def clear():
    list_box.delete(0,END)
def del_one():
    list_box.delete(ACTIVE)
def ascen():
    task.sort()
    list_box.delete(0,END)
    for to in task:
        list_box.insert(END,to)
def dscen():
    task.sort()
    task.reverse()
    list_box.delete(0,END)
    for go in task:
        list_box.insert(END,go)
def change():
    list = random.choice(task)
    lbl_change.config(text=list)
    for tasks in task:
        list_box.insert(END,tasks)

#Create New Window:->
window = Tk()

#Window Designing:->
window.title("MY TODO APP")
window.configure(bg='white')
window.geometry('550x500')
window.resizable(FALSE,FALSE)

#Create Head Label:->
lbl_head = Label(window,text="**TO-DO-LIST**",font = "Helvetica 16 bold",fg="purple",bg="white",bd=5)
lbl_head.place(x=220,y=1)
lbl_change = Label(window,text="Random task show hare!",width=25,font="Helvetica 10 bold italic",fg="black",bd=7)
lbl_change.place(x=300,y=60)

#Create Buttons:->
btn_add = Button(window,text="Add Task",width=18,font="Helvetica 10 bold",fg="purple",bg="white",bd=1,command=add)
btn_add.place(x=360,y=107)
btn_clear = Button(window,text="clear  All  Task",font="Helvetica 10 bold",fg="blue",bg="white",bd=5,command=clear)
btn_clear.place(x=30,y=340)
btn_asc = Button(window,text="Delete Task",width=11,font="Helvetica 10 bold",fg="red",bg="white",bd=5,command=del_one)
btn_asc.place(x=150,y=340)
btn_desc = Button(window,text="Sort Ascending",font="Helvetica 10 bold",fg="purple",bg="white",bd=5,command=ascen)
btn_desc.place(x=265,y=340)
btn_desc = Button(window,text="Sort Descending",font="Helvetica 10 bold",fg="purple",bg="white",bd=5,command=dscen)
btn_desc.place(x=390,y=340)
btn_rdm = Button(window,text="Choose Random",width=30,font="Helvetica 10 bold",fg="blue",bg="white",bd=5,command=change)
btn_rdm.place(x=30,y=60)
btn_ttl = Button(window,text="Total Task",width=20,font="Helvetica 10 bold",fg="red",bg="white",bd=5)
btn_ttl.place(x=95,y=380)
btn_exit = Button(window,text="Exit",width=20,font="Helvetica 12 bold",fg="black",bg="yellow",bd=5,command=exit)
btn_exit.place(x=280,y=380)

#Create Entry Box:->
entry_box = Entry(window,text="hello",width=53,bd=5,bg="#C6E2FF")
entry_box.place(x=30,y=108)

#Create List Box:->
list_box = Listbox(window,width=78,height=9,bd=8,bg="#E8DAEF")
list_box.place(x=30,y=160)

#stop terminate window:->
window.mainloop()