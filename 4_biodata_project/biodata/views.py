from django.shortcuts import render

# Create your views here.
def home(request):
    data = {}
    if request.method=='POST':
        data={
            'name': request.POST['name'],
            'age': request.POST['age'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'addr': request.POST['addr']
        }
        return render(request, 'result.html', {"data":data})
    return render(request, 'form.html')