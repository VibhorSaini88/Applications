#Create Modules:->
import requests
import  tkinter
from tkinter import *
import datetime
from datetime import date

#create method:->
def show():
    root.geometry("500x500")
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
label = Label(root,text="CITY NAME  >",bg="pink",font="times 12 bold",bd=8)
label.place(x=90,y=5)

#Create Insert Box:->
entry_box = Entry(root,bg="#0EDFD0",bd=8,width=30)
entry_box.place(x=240,y=8)
entry_box.focus()

#Create Buttons:->
bttn = Button(root,text="Show Weather",bg="orange",font="times 8 bold",bd=8,width=25,command=show)
bttn.place(x=240,y=50)

#Show result in Labels:->
city=Label(root,text="",font=30,bg='light blue',width=10)
city.place(x=243,y=100)
date=Label(root,text="",font=30,bg='#%02x%02x%02x' % (240, 160, 237),width=10)
date.place(x=340,y=100)
temp=Label(root,text="Temperature  :-",font=10,bg='red',width=15)
temp.place(x=15,y=140)
la=Label(root,text="",bg='red')
la.place(x=243,y=140)
wind=Label(root,text="Wind Speed  :-",font=10,bg='red',width=15)
wind.place(x=15,y=165)
la1=Label(root,text="",bg='red')
la1.place(x=243,y=165)
latitude=Label(root,text="Latitude  :-",font=10,bg='red',width=15)
latitude.place(x=15,y=190)
la2=Label(root,text="",bg='red')
la2.place(x=243,y=190)
longitude=Label(root,text="Longitude  :-",font=10,bg='red',width=15)
longitude.place(x=15,y=215)
la3=Label(root,text="",bg='red')
la3.place(x=243,y=215)
description=Label(root,text="Description  :-",font=10,bg='red',width=15)
description.place(x=15,y=240)
la4=Label(root,text="",bg='red')
la4.place(x=243,y=240)
pressure=Label(root,text="Pressure :-",font=10,bg='red',width=15)
pressure.place(x=15,y=265)
la5=Label(root,text="",bg='red')
la5.place(x=243,y=265)
temp_max=Label(root,text="Temperature Max :-",font=10,bg='red')
temp_max.place(x=15,y=290)
la6=Label(root,text="",bg='red')
la6.place(x=243,y=290)
temp_min=Label(root,text="Temperature Min :-",font=12,bg='red',width=15)
temp_min.place(x=15,y=315)
la7=Label(root,text="",bg='red')
la7.place(x=243,y=315)
humidity=Label(root,text="Humidity :-",font=10,bg='red',width=15)
humidity.place(x=15,y=340)
la8=Label(root,text="",bg='red')
la8.place(x=243,y=340)


root.mainloop()