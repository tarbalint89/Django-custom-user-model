from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from account.forms import RegistrationForm
from . import models


def home(request):
    context = {}
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
    return render("home")