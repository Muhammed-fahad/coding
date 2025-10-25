from datetime import datetime

# User Management
class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id     # Encapsulation
        self._name = name
        self._email = email

    def display_user(self):
        print(f"User: {self._name}, Email: {self._email}")


class Admin(User):  # Inheritance
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def display_user(self):  # Polymorphism
        print(f"[ADMIN] {self._name} ({self._email})")

    def manage_products(self):
        print(f"Admin {self._name} is managing products.")


# Product Management
class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def display_product(self):
        print(f"{self._name}: ₹{self._price} | Stock: {self._stock}")

    def update_stock(self, quantity):
        self._stock += quantity
        print(f"Updated stock for {self._name}: {self._stock}")

    def is_available(self, quantity):
        return self._stock >= quantity


# Order Processing
class Order:
    def __init__(self, order_id, user, product, quantity):
        self._order_id = order_id
        self._user = user
        self._product = product
        self._quantity = quantity
        self._date = datetime.now()

    def process_order(self):
        if self._product.is_available(self._quantity):
            self._product.update_stock(-self._quantity)
            print(f"✅ Order {self._order_id}: {self._quantity} x {self._product._name} by {self._user._name} on {self._date.strftime('%Y-%m-%d %H:%M')}")
        else:
            print(f"❌ Order {self._order_id}: Not enough stock for {self._product._name}")


# ========== DEMO ==========
if __name__ == "__main__":
    # Users
    user1 = User(1, "Fahd", "fahd@example.com")
    admin1 = Admin(100, "Admin", "admin@shop.com")

    user1.display_user()
    admin1.display_user()
    admin1.manage_products()

    print("\n--- Product Section ---")
    # Products
    p1 = Product(1, "Laptop", 55000, 10)
    p2 = Product(2, "Smartphone", 20000, 5)
    p1.display_product()
    p2.display_product()

    print("\n--- Order Section ---")
    # Orders
    order1 = Order(1, user1, p1, 2)
    order1.process_order()

    order2 = Order(2, user1, p2, 6)  # Will fail
    order2.process_order()

    print("\n--- Updated Product Info ---")
    p1.display_product()
    p2.display_product()
