from django.db import models
import datetime
from django.utils import timezone
from jdatetime import datetime

class BaseModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')

    class Meta:
        abstract = True


class BaseModel_photo(models.Model):
    phone = models.CharField(max_length=15, verbose_name='تلفن')

    class Meta:
        abstract = True


class Category(BaseModel):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'


class Customer(BaseModel_photo):
    first_name = models.CharField(max_length=255, blank=True, verbose_name='نام کوچک')  # Fixed typo here
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=255, unique=True, verbose_name='ایمیل')
    password = models.CharField(max_length=255, verbose_name='رمز عبور')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'مشتریان'
        verbose_name_plural = 'مشتریان'


class Product(BaseModel):
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name='قیمت')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='دسته‌بندی')
    description = models.TextField(blank=True, null=True, max_length=250, default="", verbose_name='توضیحات')
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name='تصویر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

def persian_now():
    return datetime.now()


class Order(BaseModel_photo):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشتری')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    address = models.TextField(max_length=500, verbose_name='آدرس')
    date = models.DateTimeField(default=persian_now, verbose_name='تاریخ')
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "در انتظار"),
            ("Shipped", "ارسال شد"),
            ("Delivered", "تحویل داده شد"),
            ("Cancelled", "لغو شد"),
        ],
        default="Pending",
        verbose_name='وضعیت'
    )

    def __str__(self):
        return f"Order #{self.id} for {self.customer}"

    class Meta:
        verbose_name = 'سفارش ها'
        verbose_name_plural = 'سفارش ها'