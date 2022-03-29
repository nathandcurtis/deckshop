from urllib.parse import parse_qsl
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .models import Card

def index(request):
    cards = Card.objects.order_by('name')
    template = loader.get_template('cards/index.html')
    context = {
        'cards': cards,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    card = Card.objects.filter(number = id)[0]
    template = loader.get_template('cards/detail.html')
    context = {
        'card': card,
    }
    return HttpResponse(template.render(context, request))   

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Username and Password do not match our records')
            return redirect('home')

    else:
        return render(request, 'cards/home.html', {}) 

    