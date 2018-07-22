#Create Modules:->
import requests
import  tkinter
from tkinter import *
import datetime
from datetime import date

#create method:->
def show():
    root.geometry("400x500")
    x = entry_box.get()

    if x != "":

        url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=c6efb3a6470e111b194bbb6f28160609&units=metric'.format(x)

        res = requests.get(url)
        data = res.json()
    else:
        entry_box.insert(END,"Invalid Entry")

    temp = str(data['main']['temp']) + ' degree celcius'
    wind_speed = str(data['wind']['speed']) + ' m/s'
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    pressure = str(data['main']['pressure']) + ' hPa'
    temp_max = str(data['main']['temp_max']) + ' degree celsius'
    temp_min = str(data['main']['temp_max']) + ' degree celsius'
    humidity = str(data['main']['humidity']) + ' %'
    name = data['name']

    current_date = datetime.date.today()

    date.config(text=current_date)
    city.config(text=name)
    la.config(text=temp)
    la1.config(text=wind_speed)
    la2.config(text=latitude)
    la3.config(text=longitude)
    la4.config(text=description)
    la5.config(text=pressure)
    la6.config(text=temp_max)
    la7.config(text=temp_min)
    la8.config(text=humidity)
#Create GUI Window:->
root = tkinter.Tk()
root.config(bg="light green")
root.title("SUNSHINE")
root.geometry("500x500")
root.resizable(FALSE,FALSE)

#Create Label:->
label = Label(root,text="CITY NAME  >",bg="pink",font="times 8 bold",bd=8)
label.place(x=50,y=5)

#Create Insert Box:->
entry_box = Entry(root,bg="#0EDFD0",bd=8)
entry_box.grid(row=1,column=2)
entry_box.focus()

#Create Buttons:->
bttn = Button(root,text="Show Weather",bg="orange",font="times 8 bold",bd=8,width="16",command=show)
bttn.place(x=260,y=70)

#Show result in Labels:->
city=Label(root,text="",font=30,bg='light blue')
city.grid(row=4,column=1,pady=5)
date=Label(root,text="",font=30,bg='#%02x%02x%02x' % (240, 160, 237))
date.grid(row=5,column=1,pady=5)
temp=Label(root,text="Temperature  :-",font=10,bg='red')
temp.grid(row=6,column=0)
la=Label(root,text="",bg='red')
la.grid(row=6,column=1)
wind=Label(root,text="Wind Speed  :-",font=10,bg='red')
wind.grid(row=7,column=0)
la1=Label(root,text="",bg='red')
la1.grid(row=7,column=1)
latitude=Label(root,text="Latitude  :-",font=10,bg='red')
latitude.grid(row=8,column=0)
la2=Label(root,text="",bg='red')
la2.grid(row=8,column=1)
longitude=Label(root,text="Longitude  :-",font=10,bg='red')
longitude.grid(row=9,column=0)
la3=Label(root,text="",bg='red')
la3.grid(row=9,column=1)
description=Label(root,text="Description  :-",font=10,bg='red')
description.grid(row=10,column=0)
la4=Label(root,text="",bg='red')
la4.grid(row=10,column=1)
pressure=Label(root,text="Pressure :-",font=10,bg='red')
pressure.grid(row=11,column=0)
la5=Label(root,text="",bg='red')
la5.grid(row=11,column=1)
temp_max=Label(root,text="Temperature Max :-",font=10,bg='red')
temp_max.grid(row=12,column=0)
la6=Label(root,text="",bg='red')
la6.grid(row=12,column=1)
temp_min=Label(root,text="Temperature Min :-",font=10,bg='red')
temp_min.grid(row=13,column=0)
la7=Label(root,text="",bg='red')
la7.grid(row=13,column=1)
humidity=Label(root,text="Humidity :-",font=10,bg='red')
humidity.grid(row=14,column=0)
la8=Label(root,text="",bg='red')
la8.grid(row=14,column=1)


root.mainloop()