from django.db import models
import random

# Create your models here.

# Function to generate a unique 5-digit user_id and order_id
def generate_id(model, field):
    """Generates a random 5-digit ID and ensures it's unique in the specified model and field."""
    while True:
        new_id = random.randint(10000, 99999)  # Generate a random 5-digit number
        if not model.objects.filter(**{field: new_id}).exists():  # Ensure it's unique
            return new_id
        

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)  # Unique email field
    address = models.TextField()
    order_id = models.IntegerField()  # This could also be a ForeignKey if it references another table
    food_order = models.TextField()  # Could be changed based on how you structure food orders (e.g., JSON, separate model)

    def __str__(self):
        return self.name
    

class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.CharField(max_length=100, blank=True)  

    def __str__(self):
        return self.product_name  
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_email = models.EmailField()  # Assuming this links to your Users table
    description = models.TextField()  # Product names
    status = models.IntegerField()  # Status of the order (e.g., 0 = pending, 1 = confirmed)

