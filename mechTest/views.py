import json
from django.shortcuts import redirect, render
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def owner(request):
    return render(request, 'owner.html')

def get_product(request):
    # Fetch all products from the database
    products = Products.objects.all()

    # Fetch all orders with status 0 (pending) -> received
    received_orders = Orders.objects.filter(status=1)

    # Fetch all orders with status 1 (preparing) -> done
    preparing_orders = Orders.objects.filter(status=2)

    # Fetch all orders with status 1 (rider) -> arrive
    rider_orders = Orders.objects.filter(status=3)

    # Pass the products to the template
    return render(request, 'index.html', {
        'products': products,
        'received_orders': received_orders,
        'preparing_orders': preparing_orders,
        'rider_orders': rider_orders
    })

def get_pending_orders(request):
    # Fetch all orders with status 0 (pending) -> received
    pending_orders = Orders.objects.filter(status=0)

    # Fetch all orders with status 1 (preparing) -> done
    preparing_orders = Orders.objects.filter(status=1)

    # Fetch all orders with status 1 (rider) -> arrive
    rider_orders = Orders.objects.filter(status=2)

    # Pass both sets of orders to the template
    return render(request, 'owner.html', {
        'pending_orders': pending_orders,
        'preparing_orders': preparing_orders,
        'rider_orders': rider_orders
    })

def mark_order_received(request, order_id):
    try:
        # Find the order by its ID
        order = Orders.objects.get(order_id=order_id)
        # Increment the status by 1
        order.status += 1
        order.save()

    except Orders.DoesNotExist:
        # Handle the case where the order does not exist
        return redirect('owner')  # Redirect to the orders page or handle it as needed

    # Redirect back to the orders page to show the updated list
    return redirect('owner')  # 'orders' should be the name of the route showing pending orders

@csrf_exempt
def confirm_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_names = data.get('product_names')
        total = data.get('total')

        if request.user.is_authenticated:
            user_email = request.user.email
        else:
            user_email = 'guest@example.com'  # or some other default email

        # Generate a new order ID
        order_id = generate_id(Orders, 'order_id')

        # Create a new order with the product description and a default status
        new_order = Orders(
            user_email=user_email,
            description=f"Products: {product_names}, Total: ${total}",
            order_id=order_id,
            status=0  # Status integer 0, indicating "pending"
        )
        new_order.save()

        # Return JSON response indicating success
        return JsonResponse({'status': 'success', 'redirect': 'home'})  # Return success response with redirect URL
    else:
        return JsonResponse({'status': 'invalid request'}, status=400)


def add_products(request):
    # List of products to add
    products_to_add = [
        {"product_name": "Wedding Cake", "price": 50.00, "image": "qistiz-wedding.jpg"},
        {"product_name": "Birthday Cake", "price": 30.00, "image": "qistiz-birthday.jpg"},
        {"product_name": "Soft Cookies", "price": 10.00, "image": "qistiz-cookies.jpg"},
        {"product_name": "Cheesecake", "price": 15.00, "image": "qistiz-cheesecake.jpg"},
        {"product_name": "Dessert", "price": 8.00, "image": "qistiz-desert.jpg"},
    ]

    # Loop through each product and check if it already exists before adding
    for product_data in products_to_add:
        new_product_id = generate_id(Products, 'product_id')
        product_id = new_product_id
        product_name = product_data["product_name"]
        product_price = product_data["price"]
        product_image_name = product_data["image"]

        # Check if the product already exists
        try:
            existing_product = Products.objects.get(product_name=product_name)
            # Product with the same name exists, skip adding this product
            continue  # Skip to the next product
        except ObjectDoesNotExist:
            # Product does not exist, create and save the new product
            new_product = Products(
                product_name=product_name,
                price=product_price,
                product_image=product_image_name
            )
            new_product.save()  # Save the product to the database

    return redirect('index')  # Redirect to the index page after processing



# Function to generate a unique 5-digit order_id
def generate_id(model, field):
    """Generates a random 5-digit ID and ensures it's unique in the specified model and field."""
    while True:
        new_id = random.randint(10000, 99999)  # Generate a random 5-digit number
        if not model.objects.filter(**{field: new_id}).exists():  # Ensure it's unique
            return new_id

def im_user(request):
    # Default user information
    default_name = "Shahrul Ficri"
    default_email = "shahrulficri1261@gmail.com"
    default_address = "Kampung Singapura, Tanjung Sedili"
    default_food_order = "cheesecake"

    # Check if the user already exists by email
    try:
        Users.objects.get(email=default_email)
        # User exists, redirect to index
        add_products(request)
        return redirect('index')  # Redirect to index.html
    except ObjectDoesNotExist:
        # User does not exist, create a new user
        new_order_id = generate_id(Users, 'order_id')
        new_user_id = generate_id(Users, 'user_id')

        new_user = Users(
            user_id=new_user_id,
            name=default_name,
            email=default_email,
            address=default_address,
            order_id=new_order_id,
            food_order=default_food_order
        )
        new_user.save()  # Save the new user to the database
        add_products(request)
        return redirect('index')  # Redirect to index.html after insertion



def im_owner(request):
    # Default user information
    default_name = "Sitiaisyah Balqis"
    default_email = "sitiaisyahbalqis@gmail.com"

    # Check if the user already exists by email
    try:
        Owner.objects.get(email=default_email)
        # User exists, redirect to index
        add_products(request)
        get_pending_orders(request)
        return redirect('owner')  # Redirect to index.html
    except ObjectDoesNotExist:
        # User does not exist, create a new user
        new_owner_id = generate_id(Owner, 'owner_id')

        new_owner = Owner(
            owner_id=new_owner_id,
            name=default_name,
            email=default_email
        )
        new_owner.save()  # Save the new user to the database
        add_products(request)
        get_pending_orders(request)
        return redirect('owner')  # Redirect to index.html after insertion
