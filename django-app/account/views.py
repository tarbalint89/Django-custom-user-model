from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login as auth_login, logout as auth_logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from . import models


def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    context = {}
    user = request.user
    context["users"] = models.Account.objects.all()
    return render(request, "index.html", context)



def registration(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            auth_login(request, account)
            return redirect("home")
        else:
            context["registration_form"] = form
    
    else:
        form = RegistrationForm()
        context["registration_form"] = form
    
    return render(request, "register.html", context)


def login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                auth_login(request, user)
                return redirect("home")
    
    else:
        form = AccountAuthenticationForm()
        context["login_form"] = form

    return render(request, "login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("login")