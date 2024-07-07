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
