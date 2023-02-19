from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        if User.objects.filter(username = username).exists():
            print('username taken')
            messages.info(request, 'Username or email already Taken')
            return redirect('/accounts/register')
        else:
            try:
                if username != "" and password != "":
                    NewUser = User.objects.create_user(username = username, password = password)
                else:
                    messages.info(request, 'Fields must not be empty')
                    return redirect('/accounts/register')

            except:
                messages.info(request, 'Fields must not be empty')
                return redirect('/accounts/register')
            NewUser.save()
            messages.info(request, 'User created')
            return redirect('/accounts/login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            messages.info(request, 'User logged in succesfully!')
            return redirect('/')
        else:
            messages.info(request, 'Wrong user or password')
            return redirect('/accounts/login/')
    else:
        return render(request, 'logIn.html')

def logout(request):
    auth.logout(request)
    return redirect('/')