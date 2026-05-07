from django.shortcuts import render
from .models import Alumni
def home(request):
    if request.method == "POST":
        Alumni.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            passing_year=request.POST['year'],
            company=request.POST['company']
        )
    return render(request, "form.html")
def filter_year(request):
    data = []
    if request.method == "POST":
        year = request.POST['year']
        data = Alumni.objects.filter(passing_year=year)
    return render(request, "result.html", {"data": data})

