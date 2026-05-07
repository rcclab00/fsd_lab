from django.shortcuts import render
from .models import Student
def home(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            grade=request.POST['grade']
        )
    return render(request, "form.html")
def o_students(request):
    data = Student.objects.filter(grade='O')
    return render(request, "result.html", {"data": data})
