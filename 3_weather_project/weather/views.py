from django.shortcuts import render
import requests

def home(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        apiid = 'ccc9fefec03e01ae382fac2a9c6d8f9c'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiid}&units=metric'
        res = requests.get(url).json()
        if res.get('cod') == 200:
            data = {
                'city': res['name'],
                'temp': res['main']['temp'],
                'desc': res['weather'][0]['description']
            }
        else:
            data = {'error': 'Invalid city name'}
    return render(request, 'form.html', {'data': data})
