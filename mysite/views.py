from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

"""
def hello_world(request):
    #return HttpResponse("Hello World!")
    return render(request, 'hello_world.html') #修改
"""

def hello_world(request): #修改
    a = 10
    b = 5
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return render(request, 'hello_world.html',locals())

def add(request, a, b):  #新增add
    s = a + b
    return HttpResponse(s)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')