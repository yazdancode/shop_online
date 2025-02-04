from django.shortcuts import render


def cart_summary(request):
    return render(request, "cart/cart_summary.html", {})


def cart_add(request, product_id):
    pass


def cart_delete(request, product_id):
    pass


def cart_update(request, product_id, quantity):
    pass
