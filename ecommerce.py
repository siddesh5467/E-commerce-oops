class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            if product.product_id in self.items:
                self.items[product.product_id]['quantity'] += quantity
            else:
                self.items[product.product_id] = {'product': product, 'quantity': quantity}
            product.update_stock(quantity)
            print(f"{quantity} of {product.name} added to cart.")
        else:
            print(f"Not enough stock for {product.name}. Available stock: {product.stock}")

    def remove_item(self, product_id, quantity):
        if product_id in self.items:
            if self.items[product_id]['quantity'] > quantity:
                self.items[product_id]['quantity'] -= quantity
                self.items[product_id]['product'].update_stock(-quantity) # Return stock
                print(f"{quantity} of {self.items[product_id]['product'].name} removed from cart.")
            elif self.items[product_id]['quantity'] == quantity:
                product = self.items[product_id]['product']
                del self.items[product_id]
                product.update_stock(-quantity) # Return stock
                print(f"{quantity} of {product.name} removed from cart.")
            else:
                print(f"Cannot remove more than available in cart ({self.items[product_id]['quantity']}).")
        else:
            print(f"Product with ID {product_id} not in cart.")

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{product.name} (x{quantity}) - ${product.price * quantity:.2f}")
            print(f"Total: ${self.get_total():.2f}")
        print("---------------------\n")

class Order:
    def __init__(self, order_id, customer, items, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.total_amount = total_amount
        self.status = "Pending"

    def set_status(self, status):
        self.status = status
        print(f"Order {self.order_id} status updated to: {self.status}")

    def display_order(self):
        print("\n--- Order Details ---")
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print("Items:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"- {product.name} (x{quantity}) - ${product.price * quantity:.2f}")
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Status: {self.status}")
        print("---------------------\n")

# Example Usage
if __name__ == "__main__":
    # Create products
    laptop = Product(1, "Laptop", 1200.00, 10)
    keyboard = Product(2, "Keyboard", 75.00, 20)
    mouse = Product(3, "Mouse", 25.00, 50)

    # Display product info
    print("--- Available Products ---")
    laptop.display_info()
    keyboard.display_info()
    mouse.display_info()
    print("--------------------------\n")

    # Create a customer
    customer1 = Customer(101, "Alice", "alice@example.com")
    customer1.display_info()

    # Add items to the shopping cart
    customer1.shopping_cart.add_item(laptop, 1)
    customer1.shopping_cart.add_item(keyboard, 2)
    customer1.shopping_cart.add_item(mouse, 3)
    customer1.shopping_cart.add_item(laptop, 1) # Add another laptop

    # Display the cart
    customer1.shopping_cart.display_cart()

    # Remove an item from the cart
    customer1.shopping_cart.remove_item(2, 1) # Remove 1 keyboard

    # Display the cart again
    customer1.shopping_cart.display_cart()

    # Place an order
    order1 = Order(1001, customer1, customer1.shopping_cart.items.copy(), customer1.shopping_cart.get_total())
    order1.display_order()

    # Update order status
    order1.set_status("Shipped")

    # Display product stock after order
    print("--- Product Stock After Order ---")
    laptop.display_info()
    keyboard.display_info()
    mouse.display_info()
    print("-------------------------------\n")
    
