from django.shortcuts import render
from .models import Student
def home(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            dept=request.POST['dept'],
            grade=request.POST['grade']
        )
    return render(request, "form.html")
def update_grade(request):
    if request.method == "POST":
        name = request.POST['name']
        new_grade = request.POST['grade']
        Student.objects.filter(name=name).update(grade=new_grade)
    data = Student.objects.all()
    return render(request, "result.html", {"data": data})

