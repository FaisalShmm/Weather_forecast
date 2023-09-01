'''Faisal Shamim'''
#importing required details
import requests
#taking city input
city=input("INPUT CITY NAME::")
print(city)
#displaying 
print("DISPLAYING WEATHER REPORT FOR {}".format(city))
#fetch weather details
url='https://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)