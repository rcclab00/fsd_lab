from django.shortcuts import render
from .models import Student
def home(request):
    if request.method == "POST":
        Student.objects.create(
            usn=request.POST['usn'],
            name=request.POST['name'],
            company=request.POST['company']
        )
    return render(request, "form.html")
def amazon_students(request):
    data = Student.objects.filter(company__iexact='Amazon')   # case-insensitive
    return render(request, "result.html", {"data": data})

