from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from home.models import UserProfile

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                messages.error(request, 'Username already exists!')
                return render(request, 'signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], 
                    password=request.POST['password1'],
                    first_name=request.POST['name'],
                    email=request.POST['email']
                )
                user_profile = UserProfile.objects.create(user=user)
                user_profile.fullName = request.POST['name']
                user_profile.Email = request.POST['email']
                user_profile.save()
                auth_login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Passwords must match.')
            return render(request, 'signup.html')
    return render(request, 'signup.html')
