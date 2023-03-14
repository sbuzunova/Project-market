from django.shortcuts import render
from products.models import *
from order.models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.
def base(request):
    return render(request, 'adminpanel/base.html')
def products(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        price=request.POST.get('price')
        category=request.POST.get('category')
        image=request.FILES.get('image')
        size=request.POST.get('size')
        maker=request.POST.get('maker')
        material=request.POST.get('material')
        if title and description and price and category and image and size and maker and material:
            category = ProductType.objects.get(pk = category)
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            file_url = fss.url(file)
            Product.objects.create(name=title, discription=description, price=price, image=file_url, product_type=category, size=size, maker=maker, material=material)
    context={
        'products': Product.objects.all(),
        'product_types': ProductType.objects.all(),
    }
    context['current_page']=1
    return render(request, 'adminpanel/products.html', context)
def category(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        if title:
            ProductType.objects.create(name=title)
    context={
        'product_types': ProductType.objects.all()
    }
    context['current_page']=3
    return render(request, 'adminpanel/category.html', context)
def orders(request, id=None):
    current_order = None
    current_products = None
    if id is not None:
        current_order = Order.objects.get(pk=id)
        current_products = current_order.products.all()
        if request.method == "POST":
            status = request.POST.get('status')
            current_order.status = status
            current_order.save()
    orders = Order.objects.all()
    status_list = ['Чекає на оплату', "Готуємо до відправки", "Відправленно", "На пошті", "Доставлено"]
    list_orders = [
        {
        "order": order,
        "status": status_list[order.status]          
        } for order in orders
    ]
    context = {
        "order_list":list_orders,
        "current_order":current_order,
        "current_products":current_products,
        "current_page":2
    }
    return render(request, 'adminpanel/orders.html', context)