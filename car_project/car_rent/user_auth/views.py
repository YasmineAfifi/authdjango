from django.shortcuts import render
from .forms import RegisterForm
from .models import Register
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
    else:
        user=RegisterForm()
        
    return render(request,'user_auth/register.html',{'rf':user})
            
    

def get_login(request):
    if request.method == 'POST':
        user_email   = request.POST.get('email')
        user_password= request.POST.get('password')
        user = authenticate(request, email=user_email, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('home')        
             
    return render(request,'user_auth/login.html')
