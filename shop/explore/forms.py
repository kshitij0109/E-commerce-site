from django import forms
from .models import Product, Buy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Product_name', 'description', 'photo1', 'photo2', 'photo3', 'price', 'category']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')





from django import forms

class BuyForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    buyer_name = forms.CharField(max_length=100, label='Your Name')
    buyer_email = forms.EmailField(label='Your Email')
    location = forms.CharField(max_length=255, label='Location')
    pincode = forms.CharField(max_length=6, min_length=6, label='Pincode', 
                              widget=forms.TextInput(attrs={'pattern': '[0-9]{6}', 'title': 'Enter a 6-digit pincode'}))
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('upi', 'UPI'),
    ]
    payment_mode = forms.ChoiceField(choices=PAYMENT_CHOICES, initial='cod', label='Mode of Payment')