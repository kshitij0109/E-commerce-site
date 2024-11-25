from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo1 = models.ImageField(upload_to='photo1/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='photo2/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='photo3/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    sold_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.Product_name[:20]}'
    


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)  
    sold_count = models.PositiveIntegerField(default=0)# Change to CharField to match the form   
    payment_mode = models.CharField(max_length=10, choices=[('cod', 'Cash on Delivery'), ('upi', 'UPI')], default='cod')  # Add this line