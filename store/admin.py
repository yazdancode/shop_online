from django.contrib import admin
from .models import Profile, Category, Customer, Product, Order
import jdatetime


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "date_modified_shamsi")
    search_fields = ("user__username", "phone")

    def date_modified_shamsi(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.date_modified).strftime(
            "%Y/%m/%d - %H:%M"
        )

    date_modified_shamsi.short_description = "تاریخ ویرایش (شمسی)"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email")
    search_fields = ("first_name", "last_name", "phone", "email")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_sale", "sale_price")
    list_filter = ("category", "is_sale")
    search_fields = ("name", "category__name")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("product", "customer", "quantity", "persian_order_date", "status")
    list_filter = ("status",)
    search_fields = ("product__name", "customer__first_name", "customer__last_name")

    def persian_order_date(self, obj):
        return jdatetime.date.fromgregorian(date=obj.date).strftime("%Y/%m/%d")

    persian_order_date.short_description = "تاریخ سفارش (شمسی)"
