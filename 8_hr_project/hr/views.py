from django.shortcuts import render
from .models import Employee
def home(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date_of_hiring=request.POST['date'],
            job_title=request.POST['job'],
            salary=request.POST['salary']
        )
    return render(request, "form.html")
def high_salary(request):
    data = Employee.objects.filter(salary__gt=50000)
    return render(request, "result.html", {"data": data})
