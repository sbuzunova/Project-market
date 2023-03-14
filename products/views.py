from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.
def base1(request):
    return render(request, 'products/base.html')
def main(request):
    type = ProductType.objects.all()
    products = search_products(request)
    print(products)
    if products:
        context = {
            'products': products
        }
    else:
        context ={
            'content' : [{
                'product_type' : product_type,
                'products' : Product.objects.filter(product_type=product_type) 
            } for product_type in type]
        }
    return render(request, 'products/main.html', context)
def product(request, id):
    products = search_products(request)
    if products:
        return main(request)
    else:
        product = Product.objects.get(pk=id)
        context ={
            'product': product,
        }
        return render(request, 'products/product.html', context)
def search_products(request):
    if request.method == 'POST':
        products = list()
        search= request.POST.get('search')
        if search:
            products = list(Product.objects.filter(
                Q(name__icontains=search) | Q(discription__icontains=search) |
                 Q(maker__icontains=search) | Q(material__icontains=search)
            ))
            categories = list(ProductType.objects.filter(Q(name__icontains=search)))
            print(categories)
            for category in categories:
                products.extend(list(Product.objects.filter(product_type=category)))
            return set(products)
def redirect_to_main(request):
    return redirect('main')