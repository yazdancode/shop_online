from django.shortcuts import render
from .models import Product
from  django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html", {})


# def search(request):
#     query = request.GET.get('q', '')
#     results = Product.objects.filter(name__icontains=query) if query else []

#     return render(request, 'home/navbar.html', {'results': results, 'query': query})


def login_user(request):
    return render(request, "home/login.html", {})


def logout_user(request):
    pass
