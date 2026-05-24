from django.shortcuts import render
from django.utils.html import escape

def home(request):
    raw=''
    safe=''
    if request.method == 'POST':
        raw = request.POST['name']       # unsafe (XSS demo)
        safe = escape(raw)               # sanitized
    return render(request, 'form.html', {'raw': raw, 'safe': safe})
