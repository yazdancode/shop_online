from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request,"home/index.html",{"products": products})


def about(request):
    return render(request, "home/about.html")


# TODO: not save session in email and phone
def login_user(request):
    if request.method == "POST":
        phone = request.POST['phone']  # دریافت شماره تلفن از فرم
        user = authenticate(request, phone=phone)  # احراز هویت با شماره تلفن
        if user is not None:
            login(request, user)  # ورود به سیستم
            messages.success(request, 'شما با موفقیت وارد شدید.')  # پیام موفقیت
            return redirect('verify_code')  # هدایت به صفحه تایید کد
        else:
            messages.error(request, 'کاربری با این شماره تلفن پیدا نشد.')  # پیام خطا
            return redirect('login')  # هدایت به صفحه ورود

    else:
        return render(request, "home/login.html", {})  # نمایش فرم ورود در صورت درخواست GET

# TODO: not save session in email and phone
#TODO: error MultiValueDictKeyError at /login/password/
def verify_code(request):
    if request.method == "POST":
        password = request.POST['password']  # دریافت رمز عبور از فرم
        user = authenticate(request, password=password)  # احراز هویت با رمز عبور
        if user is not None:
            login(request, user)  # ورود به سیستم
            messages.success(request, 'شما با موفقیت وارد شدید.')  # پیام موفقیت
            return redirect('home')  # هدایت به صفحه اصلی
        else:
            messages.error(request, 'رمز عبور نادرست است.')  # پیام خطا
            return redirect('login')  # هدایت به صفحه ورود

    else:
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
