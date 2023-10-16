from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PizzaOrder

# Create your views here.

def Greeting(request):
    page = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(page)


def otherGreeting(request):
    return render(request, "greet.html", {"title": "greetings", "message": "hello world"})


def calculateSelection(request):
    return render(request, "pizzaselect.html")

def displaySelection(request):
    price = float(request.POST["price"])
    amount = price
    return render (request, "pizzaselectoutput.html", {"selection": amount})

def order_pizza(request):
     if request.method == 'POST':
        # Get the form data from the POST request
        pizza_type = request.POST.get('pizza_type')
        pizza_size = request.POST.get('pizza_size')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not specified

        # Calculate the total price based on pizza type, size, and quantity (you can adjust prices accordingly)
        if pizza_size == 'small':
            price_per_pizza = 10.0
        elif pizza_size == 'medium':
            price_per_pizza = 15.0
        elif pizza_size == 'large':
            price_per_pizza = 20.0
        else:
            price_per_pizza = 0.0  # Invalid size

        total_price = price_per_pizza * quantity

        # Create a PizzaOrder object to save the order details (you need to define your model)
        pizza_order = PizzaOrder(pizza_type=pizza_type, pizza_size=pizza_size, quantity=quantity, total_price=total_price)
        pizza_order.save()

        # Redirect to the thank you page with the total price as a parameter
        return redirect('thank_you', total_price=total_price)


def thank_you(request, total_price):
    return render(request, 'thank_you.html', {'total_price': total_price})