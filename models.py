from django.db import models

class PizzaOrder(models.Model):
    pizza_type = models.CharField(max_length=100)  # Example: "Pepperoni", "Margherita", etc.
    pizza_size = models.CharField(max_length=50)   # Example: "small", "medium", "large", etc.
    quantity = models.IntegerField()                # Number of pizzas ordered
    total_price = models.DecimalField(max_digits=5, decimal_places=2)  # Total price of the order

    # You can add more fields as needed, such as customer information, order date, etc.

    def __str__(self):
        return f"{self.pizza_type} ({self.pizza_size}) - Quantity: {self.quantity}"