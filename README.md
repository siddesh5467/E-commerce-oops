Simple E-commerce OOP Example
This project provides a basic example of an e-commerce system implemented using Object-Oriented Programming (OOP) principles in Python. It demonstrates fundamental concepts like products, customers, shopping carts, and orders.

Classes
The project includes the following classes:

Product: Represents a product with properties like ID, name, price, and stock. It includes methods to update stock and display product information.
Customer: Represents a customer with properties like ID, name, and email. Each customer has a ShoppingCart associated with them. It includes a method to display customer information.
ShoppingCart: Represents a customer's shopping cart. It manages items (products and quantities) added by the customer. It includes methods to add and remove items, calculate the total amount, and display the cart's contents.
Order: Represents an order placed by a customer. It stores order details like ID, customer information, items ordered, total amount, and order status. It includes methods to update the order status and display order details.
How to Run
Clone the repository (or copy the code): If this code is part of a larger project, you would typically clone the repository. If you are running this in a Colab notebook, you already have the code.
Execute the Python script (or Colab cells): Run the Python file containing the code. In a Colab notebook, simply run the code cells in order.
The if __name__ == "__main__": block at the end of the script provides an example of how to use the classes to simulate a simple e-commerce flow:

Creating products
Creating a customer
Adding and removing items from the shopping cart
Placing an order
Updating the order status
Displaying product stock after the order
Project Structure
The project is structured as a single Python file containing all the class definitions and example usage.
