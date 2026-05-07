from django.shortcuts import render
from .models import Faculty
def home(request):
    if request.method == "POST":
        Faculty.objects.create(
            fid=request.POST['fid'],
            title=request.POST['title'],
            name=request.POST['name'],
            branch=request.POST['branch']
        )
    return render(request, "form.html")
def cse_professors(request):
    data = Faculty.objects.filter(
        branch__iexact='CSE',
        title__iexact='Professor'
    )
    return render(request, "result.html", {"data": data})
