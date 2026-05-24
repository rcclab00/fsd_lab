from django.shortcuts import render
from .models import Student

def home(request):
    if request.method == 'POST':
        Student.objects.create(
            usn=request.POST['usn'],
            name=request.POST['name'],
            subject_code=request.POST['subject'],
            cie_marks=request.POST['marks']
        )
    data = Student.objects.filter(cie_marks__lt=20)
    return render(request, 'form.html', {'data': data})
