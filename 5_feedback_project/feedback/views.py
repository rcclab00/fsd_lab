from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback

def home(request):
    return render(request, 'form.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        fb   = request.POST['feedback']
        Feedback.objects.create(name=name, feedback=fb)
        return JsonResponse({'name': name, 'feedback': fb})
