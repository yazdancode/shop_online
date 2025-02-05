from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import jdatetime


def persian_now():
    return jdatetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    phone = models.CharField(max_length=20, blank=True, verbose_name="شماره تلفن")
    address1 = models.CharField(max_length=200, blank=True, verbose_name="آدرس ۱")
    address2 = models.CharField(max_length=200, blank=True, verbose_name="آدرس ۲")
    city = models.CharField(max_length=200, blank=True, verbose_name="شهر")
    state = models.CharField(max_length=200, blank=True, verbose_name="استان")
    zipcode = models.CharField(max_length=200, blank=True, verbose_name="کد پستی")
    country = models.CharField(max_length=200, blank=True, verbose_name="کشور")
    old_cart = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="سبد خرید قبلی"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام دسته‌بندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=10, verbose_name="شماره تلفن")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    password = models.CharField(max_length=100, verbose_name="رمز عبور")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    price = models.DecimalField(
        default=0, decimal_places=2, max_digits=6, verbose_name="قیمت"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, verbose_name="دسته‌بندی"
    )
    description = models.CharField(
        max_length=250, default="", blank=True, null=True, verbose_name="توضیحات"
    )
    image = models.ImageField(upload_to="uploads/product/", verbose_name="تصویر محصول")
    is_sale = models.BooleanField(default=False, verbose_name="تخفیف دارد؟")
    sale_price = models.DecimalField(default=persian_now, decimal_places=2, max_digits=6, verbose_name="قیمت تخفیفی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="مشتری"
    )
    quantity = models.IntegerField(default=1, verbose_name="تعداد")
    address = models.CharField(
        max_length=100, default="", blank=True, verbose_name="آدرس"
    )
    phone = models.CharField(
        max_length=20, default="", blank=True, verbose_name="شماره تلفن"
    )
    date = models.DateField(default=persian_now, verbose_name="تاریخ سفارش")
    status = models.BooleanField(default=False, verbose_name="وضعیت ارسال")

    def persian_date(self):
        return jdatetime.date.fromgregorian(date=self.date).strftime("%Y/%m/%d")

    def __str__(self):
        return f"{self.product.name} - {self.persian_date()}"

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"
