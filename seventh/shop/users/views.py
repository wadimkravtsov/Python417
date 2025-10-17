from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                messages.success(request, 'Вы успешно авторизированны')
                return redirect('index')
    else:
        form = UserLoginForm()
    content = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', content)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    content = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', content)

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Store - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', context)