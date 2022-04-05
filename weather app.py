from tkinter import *
import tkinter as tk
from tkinter import font
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getweather():
    try:
        city = text_feild.get()
        geolocator = Nominatim(user_agent="geoapiExersises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude,lat = location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text="Current Weather")

        # Weather
        api= "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0707db83fd5d92e29c05664b679f1cc1"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        t.config(text = (temp,"°"))
        c.config(text = (condition,"|","Feels","Like",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)
        d.config(text=description)
    
    except Exception as e:
        messagebox.showinfo("weather app","Invalid input")


root = Tk()
root.title("Weather App")
root.geometry("900x500")
root.resizable(False,False)

# Search bar
search_image = PhotoImage(file = r'D:\python projects\tkinter\Weather app\images\search.png')
my_image = Label(root,image=search_image)
my_image.place(x=40,y=200)

text_feild = Entry(root,justify ="center",width=25, font=("poppins",18,"bold"),bg = "#404040",border=0,fg="white")
text_feild.place(x=52,y=40)
text_feild.focus()

search_image = PhotoImage(file=r'D:\python projects\tkinter\Weather app\images\search_icon.png')
myimage_icon = Button(image=search_image,borderwidth=0,cursor="hand2",command=getweather)
myimage_icon.place(x=400,y=34)

# LOGO
logo_image = PhotoImage(file=r'D:\python projects\tkinter\Weather app\images\logo.png')
my_logo = Label(root,image=logo_image)
my_logo.place(x=100,y=100)

# Bottom Box
bottom_image = PhotoImage(file=r'D:\python projects\tkinter\Weather app\images\box.png')
myb_image = Label(root,image=bottom_image)
myb_image.pack(side=BOTTOM,padx=5,pady=20)

# TIME
name = Label(root,font=("Arial",15,"bold"))
name.place(x=670,y=150)
clock = Label(root,font = ("helvetica",20))
clock.place(x=670,y=180)


# labels
Label1 = Label(text="WIND", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
Label1.place(x=120,y=390)

Label2 = Label(text="HUMIDITY", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
Label2.place(x=250,y=390)

Label3 = Label(text="DISCRIPTION", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
Label3.place(x=430,y=390)

Label4 = Label(text="PRESSURE", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
Label4.place(x=650,y=390)

t = Label(font=("Arial",70,"bold"),fg="#ee666f")
t.place(x=400,y=150)

c = Label(font=("Arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=130,y=420)

h = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=420)

d = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=420)

p = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=680,y=420)

root.mainloop()