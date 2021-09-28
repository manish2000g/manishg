from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.forms import LoginForm
from accounts.auth import unauthenticated_user, admin_only,user_only
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'accounts/homepage.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user credentials")
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to signup user')
            return render(request, 'accounts/signup.html', {'form_signup': form})
    context = {
        'form_signup': UserCreationForm,
        'activate_signup': 'active'
    }
    return render(request, 'accounts/signup.html', context)