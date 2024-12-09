from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials, please try again.')
            return render(request, 'login.html')
    return render(request, 'login.html')
