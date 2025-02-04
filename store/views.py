from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import SignUpForm
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
        else:
            messages.error(request, "لطفا شماره تلفن خود را وارد کنید.")
        return redirect("login")
    return render(request, "home/login.html")


def verify_code(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password:
            user = authenticate(request, password=password)
            if user is not None:
                login(
                    request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
                messages.success(request, "شما با موفقیت وارد شدید.")
                return redirect("home")
            else:
                messages.error(request, "رمز عبور نادرست است.")
        else:
            messages.error(request, "لطفا رمز عبور خود را وارد کنید.")
        return redirect("verify_code")
    return render(request, "home/verify_code.html")


def terms(request):
    try:
        return render(request, "home/terms.html")
    except Exception:
        messages.error(request, "صفحه قوانین در دسترس نیست.")
        return redirect("home")


def privacy(request):
    try:
        return render(request, "home/privacy.html")
    except Exception:
        messages.error(request, "صفحه حریم خصوصی در دسترس نیست.")
        return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید.")
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "ثبت‌نام با موفقیت انجام شد.")
                return redirect("home")
        else:
            messages.error(
                request, "مشکلی در ثبت‌نام رخ داده است. لطفا دوباره امتحان کنید."
            )
    return render(request, "home/register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "home/product.html", {"product": product})
