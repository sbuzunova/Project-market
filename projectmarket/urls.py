"""projectmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectmarket import settings
from django.conf.urls.static import static
from adminpanel.views import *
from products.views import *
from main.views import *
from order.views import *
urlpatterns = [
    path('', redirect_to_main),
    path('admin/', admin.site.urls),
    path('base/', base),
    path('products/', products),
    path('category/', category),
    path('orders/', orders),
    path('orders/<int:id>/', orders),
    path('base1/', base1),
    path('main/', main, name="main"),
    path('reg/', reg),
    path('auth/', auth, name="auth"),
    path('logout/', logout_user),
    path('product/<int:id>/', product),
    path('backet/', backet, name="backet"),
    path('add_product/<int:product_id>/', add_product),
    path('delete_product/<int:product_id>/', delete_product),
    path('createorder/', create_order),
    path('myorders/', my_orders),
    path('ordertracking/<int:id>/', order_tracking),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
