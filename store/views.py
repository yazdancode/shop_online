from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django import forms
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html")


def login_user(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        if phone:
            user = authenticate(request, phone=phone)
            if user is not None:
                login(request, user)
                messages.success(request, "شما با موفقیت وارد شدید.")
                return redirect("verify_code")
            else:
                messages.error(request, "کاربری با این شماره تلفن پیدا نشد.")
                return redirect("login")
        else:
            messages.error(request, "لطفا شماره تلفن خود را وارد کنید.")
            return redirect("login")
    else:
        return render(request, "home/login.html", {})


# TODO: not save session in email and phone
def verify_code(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password:
            user = authenticate(request, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "شما با موفقیت وارد شدید.")
                return redirect("home")
            else:
                messages.error(request, "رمز عبور نادرست است.")
                return redirect("login")
        else:
            messages.error(request, "لطفا رمز عبور خود را وارد کنید.")
            return redirect("verify_code")
    else:
        return render(request, "home/verify_code.html", {})


# TODO: not template terms.html
def terms(request):
    return render(request, "home/terms.html")


# TODO: not tempalte privacy.html
def privacy(request):
    return render(request, "home/privacy.html")


def logout_user(request):
    logout(request)
    return redirect("home")


# TODO: not register.html
# register with test writen
def register_user(request):
    return render(request, "home/register.html", {})
