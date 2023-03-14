from django.shortcuts import render, redirect
from .models import *
from products.models import Product
# Create your views here.
def backet(request):
    try:
        backet = Bucket.objects.get(user=request.user)
    except:
        backet = Bucket.objects.create(user=request.user)
    products = backet.products.all()
    context = {
        'products': products
    }
    return render(request, 'order/backet.html', context)
def add_product(request, product_id):
    try:
        backet = Bucket.objects.get(user=request.user)
    except:
        backet = Bucket.objects.create(user=request.user)
    product = Product.objects.get(id=product_id)
    backet.products.add(product)
    return redirect('main')
def delete_product(request, product_id):
    try:
        backet = Bucket.objects.get(user=request.user)
    except:
        backet = Bucket.objects.create(user=request.user)
    product = Product.objects.get(id=product_id)
    backet.products.remove(product)
    return redirect('backet')
def create_order(request):
    full_price = 0
    try:
        backet = Bucket.objects.get(user=request.user)
    except:
        backet = Bucket.objects.create(user=request.user)
    products = backet.products.all()
    for product in products:
        full_price += product.price
    if request.method == 'POST':
        post_number = request.POST.get('post_number')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        full_name = request.POST.get('full_name')
        if post_number and city and phone_number and full_name:
            order = Order.objects.create(user=request.user, status=0, full_name=full_name, post_number=post_number, phone_number=phone_number, city=city)
            for product in products:
                order.products.add(product)
            order.save()
            backet.products.clear()
            products =[]
            full_price = 0
    context = {
        'products': products,
        'full_price': full_price
    }
    return render(request, 'order/create_order.html', context)
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    status_list = ['Чекає на оплату', "Готуємо до відправки", "Відправленно", "На пошті", "Доставлено"]
    list_orders = [
        {
        "order": order,
        "full_price": sum([product.price for product in order.products.all()]),
        "status": status_list[order.status]          
        } for order in orders
    ]
    context = {
        "list_orders":list_orders
    }
    return render(request, 'order/my_orders.html', context)
def order_tracking(request, id):
    order = Order.objects.get(pk=id)
    products = order.products.all()
    context = {
        "products": products,
        "order": order
    }
    return render(request, 'order/order_tracking.html', context)