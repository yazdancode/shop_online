from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html")


# TODO: not save session in email and phone
def login_user(request):
    if request.method == 'POST':
        pass
        

    return render(request, "home/login.html", {})


# TODO: not save session in email and phone
def verify_code(request):
    if request.method == 'POST':
        pass
    return render(request, "home/verify_code.html", {})


def logout_user(request):
    logout(request)
    return redirect("home")
