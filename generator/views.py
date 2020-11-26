from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    
    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    
    pswd = ''
    for x in range(length):
        pswd += random.choice(char)
    
    return render(request, 'generator/password.html', {'password': pswd})

def about(request):
    return render(request, 'generator/about.html')