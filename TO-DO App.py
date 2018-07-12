#Import Modules:->
import tkinter
from tkinter import *
import random
from tkinter import messagebox

#create global list of task:->
list = []
#create functions:->
def add():
    list.insert(1,entry_box.get())
    list_box.insert(END,entry_box.get())
    entry_box.delete(0,END)
def clear():
    result1 = messagebox.askyesno("Clear All","Do you want to clear all task")
    if result1==1:
        list_box.delete(0,END)
    else:
        pass
def del_one():
    result2 = messagebox.askyesno("Delete_one","Do you want to delete of selected task")
    if result2==1:
         list_box.delete(ACTIVE)
    else:
        pass
def ascen():
    list.sort()
    list_box.delete(0,END)
    for to in list:
        list_box.insert(END,to)
def dscen():
    list.sort()
    list.reverse()
    list_box.delete(0,END)
    for go in list:
        list_box.insert(END,go)
def random1():
    list1 = random.choice(list)
    lbl_change.config(text=list1)
def ttl():
    box = len(list)
    lbl_change.config(text=box)
def exit():
    result = messagebox.askyesno("EXIT","Do you want to Quit?")
    if result==1:
        window.destroy()
    else:
        pass
def info():
    lbl_change1.config(text="TODO APP! MADE BY VIBHOR....")
#Create New Window:->
window = Tk()

#Window Designing:->
window.title("MY TODO APP")
window.configure(bg='purple')
window.geometry('550x510')
window.resizable(FALSE,FALSE)

#Create Head Label:->
lbl_head = Label(window,text="**TO-DO-LIST**",font = "Helvetica 16 bold",fg="purple",bg="white",bd=5)
lbl_head.place(x=220,y=1)
lbl_change = Label(window,text="Random task show hare!",width=25,font="Helvetica 10 bold italic",fg="black",bd=7)
lbl_change.place(x=300,y=60)
lbl_change1 = Label(window,text=" ",width=25,bg="white",font="Helvetica 10 bold italic",fg="brown",bd=7)
lbl_change1.place(x=295,y=470)

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
btn_rdm = Button(window,text="Choose Random",width=30,font="Helvetica 10 bold",fg="blue",bg="white",bd=5,command=random1)
btn_rdm.place(x=30,y=60)
btn_ttl = Button(window,text="Total Task",width=20,font="Helvetica 10 bold",fg="red",bg="white",bd=5,command=ttl)
btn_ttl.place(x=95,y=380)
btn_exit = Button(window,text="Exit",width=20,font="Helvetica 12 bold",fg="black",bg="yellow",bd=5,command=exit)
btn_exit.place(x=280,y=380)
btn_info = Button(window,text="info",font="Helvetica 12 bold",fg="black",bg="pink",bd=5,command=info)
btn_info.place(x=250,y=470)

#Create Entry Box:->
entry_box = Entry(window,text="hello",width=53,bd=5,bg="#C6E2FF")
entry_box.place(x=30,y=108)

#Create List Box:->
list_box = Listbox(window,width=78,height=9,bd=8,bg="#E8DAEF")
list_box.place(x=30,y=160)

#stop terminate window:->
window.mainloop()