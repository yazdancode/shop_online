from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Product, Customer
from .forms import CustomerForm


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html")


# TODO: not save session in email and phone
def login_user(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            customer = Customer(email=email, phone=phone)
            customer.save()
            return render(request, 'home/login.html')
    else:
        form = CustomerForm()

    return render(request, "home/login.html", {'form':form})


# TODO: not save session in email and phone
def verify_code(request):
    if request.method == "POST":
        pass
    return render(request, "home/verify_code.html", {})

#TODO: not template terms.html
def terms(request):
    return render(request, "home/terms.html")

#TODO: not tempalte privacy.html
def privacy(request):
    return render(request, "home/privacy.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def show_customers(request):
    customers = Customer.objects.all()
    return render(request, 'home/show_customers.html', {'customers': customers})
