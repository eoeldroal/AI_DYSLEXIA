from django.contrib import auth, messages
from django.shortcuts import redirect

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')
