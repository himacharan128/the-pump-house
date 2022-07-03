from django.shortcuts import render
from django.http import HttpResponse
from .models import formdetails

# Create your views here.
def home(request):
    if(request.POST):
        x = request.POST['name']
        y = request.POST['email']
        z = request.POST['contactnum']
        user = formdetails(name=x, email=y, contactnum=z)
        user.save()
        return render(request, 'home.html', {'name': x, 'email': y})
    return render(request, 'index.html')

def display(request):
    db = formdetails.objects.all()
    return render(request, 'display.html', {'dblist': db})

def update(request):
    user = formdetails.objects.get(name='example')
    user.email='ihaveanemail@gmail.com'
    user.save()
    return HttpResponse('<h1>User Value Updated.</h1>')

def delete(request):
    user = formdetails.objects.get(name='example')
    user.delete()
    return HttpResponse("<h1>Delete Value Successfully</h1>")