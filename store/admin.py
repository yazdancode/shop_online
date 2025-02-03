from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Customer, Order, Product


# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Displays the id and name of categories
    search_fields = ("name",)  # Allows searching by name


# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
    )  # Display key customer info
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )  # Allows searching by fields
    list_filter = ("email",)  # Allows filtering by email


# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
        "description",
        "image_preview",  # If you want a thumbnail preview of images
        "is_sale",
        "sale_price",
    )  # Display key product info
    search_fields = (
        "name",
        "category__name",
    )  # Allows searching by product name and category name
    list_filter = (
        "category",
        "is_sale",
    )  # Allows filtering by category and sale status

    # Custom image preview function
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"


# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "product",
        "quantity",
        "address",
        "status",
        "date",
    )  # Display key order info
    search_fields = (
        "customer__first_name",
        "customer__last_name",
        "product__name",
    )  # Allows searching by customer or product
    list_filter = ("status",)  # Allows filtering by order status
