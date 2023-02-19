from django.shortcuts import render, redirect
from django.http import HttpResponse


def MainPage(request):
    if request.user.is_authenticated == False:
        return render(request, 'index.html')
    else:
        return render(request, 'UserLogged.html')