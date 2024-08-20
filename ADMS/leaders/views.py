from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from leaders.models import Leader

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)  
            messages.success(request, 'Login successful')
            return redirect('login-page') 
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login-page')

    return render(request, 'leaders/login.html')



def leaders_view(request):
    return render(request,'leaders/leader.html')
