#Importing Required Libraries
from tkinter import *
import requests
import datetime 
import json
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

#Creating the main interface
root=Tk()
root.title("Weather Forecasting - Group 4")
root.geometry("890x560+300+300")
root['background']="#57adff"

#Defining API and retrieving details
def city_name():
    city=searching.get()

    #Getting Location and timezone for given location
    geolocator=Nominatim(user_agent="geoapiExcercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    time_zone=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    #Defining and Calliing API
    url="https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&appid=ec07412f864e92751f697214bdebd0aa"
    response=requests.get(url).json() 

    #Declaring API for today's data
    today="https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&exclude=hourly,daily&appid="+"ec07412f864e92751f697214bdebd0aa"
    todays_data=requests.get(today).json()
    
    #Generalising Date and Time and Printing timezone,time
    home=pytz.timezone(time_zone)
    local_time=datetime.datetime.now(home)
    current_Time=local_time.strftime("%I:%M:%S%p")
    time.config(text=current_Time)
    City.config(text=time_zone)

    #Printing the Coordinates
    lon=location.longitude
    lat=location.latitude
    coord=str(round(lon,4)) + "°N  " + str(round(lat,4)) + "°E"
    Location.config(text=coord)

    #Printing Place and Country Details
    place=todays_data['name']
    country=todays_data['sys']['country']
    label_city.config(text=(place,"/",country))

    #Printing Date and Day for today
    today_time=local_time.strftime("%a, %d/%b")
    label_date.config(text=today_time)

    #Getting neccessary details
    feels_like=todays_data['main']['feels_like']
    humidity=todays_data['main']['humidity']
    pressure=todays_data['main']['pressure']
    wind_speed=todays_data['wind']['speed']
    descrip=todays_data['weather'][0]['description']
    r_prob=response['list'][0]['pop']
    sun_rise=todays_data['sys']['sunrise']
    sun_set=todays_data['sys']['sunset']
    timegap=todays_data['timezone']

    #Displaying Neccessary Details
    t1.config(text=(feels_like,"°C"))
    t2.config(text=(humidity,"%"))
    t3.config(text=(pressure,"hPa"))
    t4.config(text=(wind_speed,"m/s"))

    #Retreiving Main Weather Details
    temp1=todays_data['main']['temp']
    temp2=todays_data['main']['temp_min']
    temp3=todays_data['main']['temp_max']

    #Setting and Displaying Main Weather Details
    current_temp=str(temp1)+"°C"
    label_temp.config(text=current_temp)
    min_temp=str(round(temp2))+"°C/"+str(round(temp3))+"°C"
    labelMinMax_temp.config(text=min_temp)
    rain_prob="Rain  "+str(round(r_prob*100))+"%"
    label_pop.config(text=rain_prob)
    label_desc.config(text=descrip)
    sunrise="Sunrise "+str(datetime.datetime.utcfromtimestamp(sun_rise+timegap).strftime("%I:%M:%S %p"))
    label_sunrise.config(text=sunrise)
    sunset="Sunset   "+str(datetime.datetime.utcfromtimestamp(sun_set+timegap).strftime("%I:%M:%S %p"))
    label_sunset.config(text=sunset)

    #Displaying the Next day
    second=first+datetime.timedelta(days=1)
    day2.config(text=second.strftime("%a, %d/%b"))    

    #Retreiving Next day weather details
    day2Temp=response['list'][1]['main']['temp']
    day2Min=response['list'][1]['main']['temp_min']
    day2Max=response['list'][1]['main']['temp_max']
    day2Desc=response['list'][1]['weather'][0]['description']

    #Displaying Day2 Weather Details
    temp_day2= str(round(day2Temp))+"°C"
    minmax_day2= str(round(day2Max))+"°C/"+str(round(day2Min))+"°C"
    day2_desc.config(text=day2Desc)
    day2_maintemp.config(text=temp_day2)
    day2_minmax.config(text=minmax_day2)

    #Displaying the Next day
    third=first+datetime.timedelta(days=2)
    day3.config(text=third.strftime("%a, %d/%b"))    

    #Retreiving Next day weather details
    day3Temp=response['list'][2]['main']['temp']
    day3Min=response['list'][2]['main']['temp_min']
    day3Max=response['list'][2]['main']['temp_max']
    day3Desc=response['list'][2]['weather'][0]['description']

    #Displaying Day2 Weather Details
    temp_day3= str(round(day3Temp))+"°C"
    minmax_day3= str(round(day3Max))+"°C/"+str(round(day3Min))+"°C"
    day3_desc.config(text=day3Desc)
    day3_maintemp.config(text=temp_day3)
    day3_minmax.config(text=minmax_day3)

    #Displaying the Next day
    fourth=first+datetime.timedelta(days=3)
    day4.config(text=fourth.strftime("%a, %d/%b"))    

    #Retreiving Next day weather details
    day4Temp=response['list'][3]['main']['temp']
    day4Min=response['list'][3]['main']['temp_min']
    day4Max=response['list'][3]['main']['temp_max']
    day4Desc=response['list'][3]['weather'][0]['description']

    #Displaying Day2 Weather Details
    temp_day4= str(round(day4Temp))+"°C"
    minmax_day4= str(round(day4Max))+"°C/"+str(round(day4Min))+"°C"
    day4_desc.config(text=day4Desc)
    day4_maintemp.config(text=temp_day4)
    day4_minmax.config(text=minmax_day4)

    #Displaying the Next day
    fifth=first+datetime.timedelta(days=4)
    day5.config(text=fifth.strftime("%a, %d/%b"))    

    #Retreiving Next day weather details
    day5Temp=response['list'][4]['main']['temp']
    day5Min=response['list'][4]['main']['temp_min']
    day5Max=response['list'][4]['main']['temp_max']
    day5Desc=response['list'][4]['weather'][0]['description']

    #Displaying Day2 Weather Details
    temp_day5= str(round(day5Temp))+"°C"
    minmax_day5= str(round(day5Max))+"°C/"+str(round(day5Min))+"°C"
    day5_desc.config(text=day5Desc)
    day5_maintemp.config(text=temp_day5)
    day5_minmax.config(text=minmax_day5)      
    
#Interface for displaying Current details
desc_box=PhotoImage(file="desc.png")
Label(root,image=desc_box,bg="#57adff",borderwidth=2,relief="solid").place(x=30,y=135)

#Adding details to description box
label1=Label(root,text="Feels like",font=('Cambria',11),fg="white",bg="#00008b")
label1.place(x=40,y=145)

label2=Label(root,text="Humidity",font=('Cambria',11),fg="white",bg="#00008b")
label2.place(x=40,y=170)

label3=Label(root,text="Pressure",font=('Cambria',11),fg="white",bg="#00008b")
label3.place(x=40,y=195)

label4=Label(root,text="Wind Speed",font=('Cambria',11),fg="white",bg="#00008b")
label4.place(x=40,y=220)

#Displaying Neccessary details
t1=Label(root,font=("Cambria",11),fg="white",bg="#00008b")
t1.place(x=135,y=145)
t2=Label(root,font=("Cambria",11),fg="white",bg="#00008b")
t2.place(x=135,y=170)
t3=Label(root,font=("Cambria",11),fg="white",bg="#00008b")
t3.place(x=135,y=195)
t4=Label(root,font=("Cambria",11),fg="white",bg="#00008b")
t4.place(x=135,y=220)

#Search Box
search_img=PhotoImage(file="Rounded Rectangle 3.png")
label6=Label(root,image=search_img,bg="#57adff")
label6.place(x=233,y=15)

search_1=PhotoImage(file="search1.png")
label7=Label(root,image=search_1,bg="#203243")
label7.place(x=245,y=20)

searching=Entry(root,justify="center",width=12,font=("calibiri",20),bg="#203243",border=0,fg="white")
searching.place(x=328,y=25)
searching.focus()

search_2=PhotoImage(file="icon.png")
label7=Button(root,image=search_2,bg="#203243",borderwidth=0,cursor="hand2",command=city_name)
label7.place(x=538,y=20)

#Bottom interface
frame=Frame(root,width=900,height=180,bg="#383838")
frame.pack(side=BOTTOM)

#Bottom description boxes
Next=PhotoImage(file="next.png")
Rem=PhotoImage(file="remaining.png")
Label(frame,image=Next,bg="#383838").place(x=45,y=20)
Label(frame,image=Rem,bg="#383838").place(x=315,y=26)
Label(frame,image=Rem,bg="#383838").place(x=495,y=26)
Label(frame,image=Rem,bg="#383838").place(x=675,y=26)

#City Time
time=Label(root,font=("Times New Roman",12),bg="#57adff",fg="black")
time.place(x=445 ,y=115)

#Timezone and Location
City=Label(root,font=("Times New Roman",16,"bold"),bg="#57adff",fg="white",justify=RIGHT)
City.place(x=680,y=10)

Location=Label(root,font=("Times New Roman",12,"bold"),bg="#57adff",fg="white",justify=RIGHT)
Location.place(x=680,y=37)

#First Bottom Box
firstframe=Frame(root,width=230,height=132,bg="white")
firstframe.place(x=50,y=405)

day2=Label(root,font=("Arial",18,"bold"),fg="black",bg="white")
day2.place(x=125,y=408)

day2_maintemp=Label(root,font=("Calibiri",16),fg="black",bg="white")
day2_maintemp.place(x=200,y=445)

day2_minmax=Label(root,font=("Calibiri",13),fg="black",bg="white")
day2_minmax.place(x=180,y=475)

day2_desc=Label(root,font=("Calibiri",13),fg="black",bg="white")
day2_desc.place(x=155,y=495)

#Second Bottom Box 
secondframe=Frame(root,width=142,height=124,bg="white")
secondframe.place(x=321.5,y=411)

day3=Label(root,font=("Arial",16,"bold"),fg="black",bg="white")
day3.place(x=337,y=415)

day3_maintemp=Label(root,font=("Calibiri",14),fg="black",bg="white")
day3_maintemp.place(x=400,y=445)

day3_minmax=Label(root,font=("Calibiri",11),fg="black",bg="white")
day3_minmax.place(x=388,y=473)

day3_desc=Label(root,font=("Calibiri",11),fg="black",bg="white")
day3_desc.place(x=324,y=495)

#Third Bottom Box
thirdframe=Frame(root,width=142,height=124,bg="white")
thirdframe.place(x=502,y=411)

day4=Label(root,font=("Arial",16,"bold"),fg="black",bg="white")
day4.place(x=515,y=415)

day4_maintemp=Label(root,font=("Calibiri",14),fg="black",bg="white")
day4_maintemp.place(x=582,y=445)

day4_minmax=Label(root,font=("Calibiri",11),fg="black",bg="white")
day4_minmax.place(x=567,y=473)

day4_desc=Label(root,font=("Calibiri",11),fg="black",bg="white")
day4_desc.place(x=505.5,y=495)

#Fourth Bottom Box
fourthframe=Frame(root,width=142,height=124,bg="white")
fourthframe.place(x=682,y=411)

day5=Label(root,font=("Arial",16,"bold"),fg="black",bg="white")
day5.place(x=692,y=415)

day5_maintemp=Label(root,font=("Calibiri",14),fg="black",bg="white")
day5_maintemp.place(x=763,y=445)

day5_minmax=Label(root,font=("Calibiri",11),fg="black",bg="white")
day5_minmax.place(x=748,y=473)

day5_desc=Label(root,font=("Calibiri",11),fg="black",bg="white")
day5_desc.place(x=685,y=495)

#Main Weather Details Box
label_temp=Label(root,font=("Cambria",25,"bold"),bg="#57adff",fg="black")
label_temp.place(x=390,y=150)

labelMinMax_temp=Label(root,font=("Cambria",22,"bold"),bg="#57adff",fg="black")
labelMinMax_temp.place(x=370,y=190)

label_pop=Label(root,font=("Cambria",18,"bold"),bg="#57adff",fg="black")
label_pop.place(x=370,y=230)

label_desc=Label(root,font=("Cambria",18,"bold"),bg="#57adff",fg="black")
label_desc.place(x=370,y=260)

#Location and Country
label_city=Label(root,font=("Times New Roman",27,"bold"),bg="#57adff",fg="black")
label_city.place(x=370,y=75)

label_date=Label(root,font=("Times New Roman",12,),bg="#57adff",fg="black")
label_date.place(x=360,y=115)

#Search Time and Date
label_stime=Label(root,font=("Times New Roman",18,"bold"),fg="#203243",bg="#57adff")
label_stime.place(x=10,y=10)

label_sdate=Label(root,font=("Times New Roman",14,"bold"),fg="#203243",bg="#57adff")
label_sdate.place(x=28,y=40)

#Sunsrise and Sunset Time
label_sunrise=Label(root,font=("Cambria",16,"bold"),fg="#00005c",bg="#57adff")
label_sunrise.place(x=680,y=290)

label_sunset=Label(root,font=("Cambria",16,"bold"),fg="#00005c",bg="#57adff")
label_sunset.place(x=680,y=320)

first=datetime.datetime.now()
label_stime.config(text=first.strftime("%I:%M %p"))
label_sdate.config(text=first.strftime("%d/%b"))

root.mainloop()