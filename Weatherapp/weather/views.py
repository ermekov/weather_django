from django.shortcuts import render
import requests
from .models import City
from .form import CityForm

def index(request):
    key = 'cced0bc6133666f728728356fda52d60'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+key

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            if not City.objects.filter(name=city_name).exists():
                form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info ={
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)
