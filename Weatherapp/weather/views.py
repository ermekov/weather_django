from django.shortcuts import render
import requests

def index(request):
    key = 'cced0bc6133666f728728356fda52d60'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+key

    city = 'London'
    res = requests.get(url.format(city)).json()
    city_info ={
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)
