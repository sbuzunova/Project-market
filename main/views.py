from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def reg(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        sucpassword = request.POST.get('sucpassword')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        if password != sucpassword:
            context['error'] = "Паролі не співпадають"
        elif len(password) < 8:
            context['error'] = "Короткий пароль"
        else:
            try:
                User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                return redirect('auth')
            except IntegrityError:
                context['error'] = "Такий користувач вже створений"
    return render(request, 'main/reg.html', context)
def auth(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('main')
        else:
            context['error'] = "Неправильне ім'я користувача або пароль"
    return render(request, 'main/auth.html', context)
def logout_user(request):
    logout(request)
    return redirect('main')