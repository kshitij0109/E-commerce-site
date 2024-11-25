from django.shortcuts import render,redirect
from .models import Product, Buy
from .forms import ProductForm, UserRegistrationForm, BuyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal



def index(request):
    return render(request, 'index.html')




def all_items(request):
    products = Product.objects.all()
    return render(request, 'all_items.html',{'products':products})


@login_required
def item_detail(request, pk):
    product = Product.objects.filter(id=pk)
    return render(request, 'item_detail.html', {'product':product})  


@login_required
def sell(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('all_items')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form':form})





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_items')
    else:
        form = UserRegistrationForm
    return render(request, 'registration/register.html', {'form':form})




def account(request):
    user = request.user
    total_items = Product.objects.filter(user=user)
    return render(request, 'account.html', {'user':user, 'total_items':total_items})


@login_required
def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('all_items')
    else:
        form = BuyForm()
    return render(request, 'buy.html', {'form':form})
       


@login_required
@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            buyer_name = form.cleaned_data['buyer_name']
            buyer_email = form.cleaned_data['buyer_email']
            location = form.cleaned_data['location']
            pincode = form.cleaned_data['pincode']
            payment_mode = form.cleaned_data['payment_mode']

          
            product.sold_count += quantity
            product.save()

           
            Buy.objects.create(
                user=request.user,
                product=product,
                Name=buyer_name,
                location=location,
                pincode=pincode,
                sold_count=quantity 
            )

           
            total_price = product.price * quantity

           
            return redirect('success', product_id=product.id, quantity=quantity, total_price=total_price)

    else:
        form = BuyForm()

    return render(request, 'product_detail.html', {'product': product, 'form': form})

def success(request, product_id, quantity, total_price):
    product = get_object_or_404(Product, id=product_id)
    total_price = Decimal(total_price) 
    return render(request, 'success.html', {
        'product': product,
        'quantity': quantity,
        'total_price': total_price,
    })



def prod_edit(request, product_id):
    tweet = get_object_or_404(Product, pk=product_id, user = request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_items')
    else:
        form = ProductForm(instance=tweet)
    return render(request, 'sell.html', {'form':form})


def prod_delete(request, product_id):
    tweet = get_object_or_404(Product, pk=product_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('all_items')
    return render(request, 'confirm.html', {'tweet':tweet})



