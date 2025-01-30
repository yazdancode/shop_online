from django.shortcuts import render, redirect
from .models import Product
from .forms import CustomerForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html", {})


def login_user(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            request.session["phone"] = phone

            user = authenticate(request, email=email, phone=phone)
            if user is not None:
                login(request, user)
                return redirect("verify_code")
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است!")
    else:
        form = CustomerForm()

    return render(request, "home/login.html", {"form": form})


def verify_code(request):
    form = CustomerForm(request.POST or None)
    message = ""

    if request.method == 'POST' and form.is_valid():
        password = form.cleaned_data["password"]
        user = authenticate(request, password=password)
        if user is not None:
            login(request, user)
            message = "ورود موفقیت آمیز بود."
        else:
            form.add_error(None, "نام کاربری یا رمز عبور اشتباه است!")

    phone = request.session.get("phone", None)
    if phone:
        message = f"کد تأیید برای شماره {phone} پیامک شد."
    elif not message:
        message = "شماره تلفن موجود نیست."

    return render(request, "home/verify_code.html", {"form": form, "message": message})


def logout_user(request):
    pass
