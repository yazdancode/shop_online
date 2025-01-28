from django.contrib import admin
from .models import Category, Customer, Product, Order


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
    )  # Display key product info
    search_fields = (
        "name",
        "category__name",
    )  # Allows searching by product name and category name
    list_filter = ("category",)  # Allows filtering by category


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
