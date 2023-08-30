from tkinter import*
import requests
import json
from datetime import datetime
from tkinter.scrolledtext import*

def f1():
	def time_format_for_location(utc_with_tz):
		local_time = datetime.utcfromtimestamp(utc_with_tz)
		return local_time.time()
	view.delete(1.0,END)
   	 # Get city name from user from the input field (later in the code)	
	city_name=loc_field.get()
   	 # API url
	a1="http://api.openweathermap.org/data/2.5/weather"
	a2="?units=metric"
	a3="&appid="+"6ff44accf9fc47a36d2810ec0ab07b5d"
	a4="&q="+city_name
	weather_url =a1+a2+a3+a4
 
    	# Get the response from fetched url
	response = requests.get(weather_url)
 
    	# changing response from json to python readable 
	weather_info = response.json()
	loc_field.delete(0,END)   #to clear the text field for every new output
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched	
	if weather_info['cod'] == 200:
		kelvin = 273 # value of kelvin
		temp = int(weather_info['main']['temp'])                                     
		feels_like_temp = int(weather_info['main']['feels_like'])
		pressure = weather_info['main']['pressure']
		humidity = weather_info['main']['humidity']
		wind_speed = weather_info['wind']['speed'] * 3.6
		sunrise = weather_info['sys']['sunrise']
		sunset = weather_info['sys']['sunset']
		timezone = weather_info['timezone']
		cloudy = weather_info['clouds']['all']
		description= weather_info['weather'][0]['description']
 
		sunrise_time = time_format_for_location(sunrise + timezone)
		sunset_time = time_format_for_location(sunset + timezone)
 
		#assigning Values to our weather varaible, to display as output
		weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"	
		
	else:
		weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
		
	view.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
main_window=Tk()
main_window.title("weather application")
main_window.geometry("700x700+100+100")
f=("Calibri",20,"bold")

loc_lab = Label(main_window,text="enter location: ",font=f)
loc_field = Entry(main_window , font=f)
loc_lab.pack(pady=10)
loc_field.pack(pady=10)
find=Button(main_window ,text="show weather",font=f,width=15,command=f1)
find.pack(pady=10)
view =ScrolledText(main_window,width=45 ,height=10 ,font=f)
view.pack(pady=10)
main_window.mainloop()
