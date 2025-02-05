from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SignUpForm
from .models import Product, Category, Profile


def home(request):
    products = Product.objects.all()
    return render(request, "home/index.html", {"products": products})


def about(request):
    return render(request, "home/about.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user, created = Profile.objects.get_or_create(user=user)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, "شما با موفقیت وارد شدید!")
            return redirect('home')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است. لطفا دوباره امتحان کنید.")
            return redirect('login')

    return render(request, 'home/login.html')




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
            return redirect('register')
    return render(request, "home/register.html", {"form": form})


def product(request, pk):
    products = Product.objects.get(id=pk)
    return render(request, "home/product.html", {"products": products})


def category(request, foo):
    foo = foo.replace("-", " ")
    categorys = get_object_or_404(Category, name=foo)

    products = Product.objects.filter(category=categorys)

    return render(
        request, "home/category.html", {"products": products, "category": categorys}
    )
