from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.messages.storage.base import Message
from django.core.mail import message
from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['password1']

        if password == confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save();
                return redirect('login')

            print("user created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
