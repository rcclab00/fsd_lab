from django.shortcuts import render, redirect
from .models import Student
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        usn = request.POST['usn']
        sem = request.POST['semester']
        fee = request.POST.get('fee') == 'on'   # checkbox
        Student.objects.create(
            name=name, usn=usn,
            semester=sem, fee_paid=fee
        )
    data = Student.objects.all()
    return render(request, "form.html", {"data": data})
def delete_unpaid(request):
    Student.objects.filter(fee_paid=False).delete()
    return redirect('/')
