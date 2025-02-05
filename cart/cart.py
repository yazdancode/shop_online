class Cart:
    def __init__(self, request):
        """Initialize the cart."""
        self.session = request.session
        cart = self.session.get("session_key", {})

        if "session_key" not in self.session:
            self.session["session_key"] = cart
        
        self.cart = cart

    def add(self, product_id, quantity=1, update_quantity=False):
        """Add a product to the cart or update its quantity."""
        product_id = str(product_id)  # کلید‌ها باید رشته باشند
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]["quantity"] = quantity
            else:
                self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {"quantity": quantity}

        self.save()

    def remove(self, product_id):
        """Remove a product from the cart."""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Remove all items from the cart."""
        self.session["session_key"] = {}
        self.save()

    def save(self):
        """Mark the session as modified to ensure changes are saved."""
        self.session.modified = True

    def __iter__(self):
        """Iterate over the items in the cart."""
        for item in self.cart.values():
            yield item

    def __len__(self):
        """Count all items in the cart."""
        return sum(item["quantity"] for item in self.cart.values())
