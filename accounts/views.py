from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        # ! get input value from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # ! check password
        if password == password2:
            # ! check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exist !")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email exist !")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered !')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match !')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logging in !')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    # messages.success(request, "You are logging out !")
    return redirect('index')


def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
