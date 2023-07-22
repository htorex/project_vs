from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

#from django.contrib.auth.models import User
from users.models import User

from .forms import Registerform

from products.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')


    return render(request,'index.html', {
        'message': 'Lista de productos',
        'title' : 'productos',
        'products' : products,
    })


def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        
        else:
            messages.error(request, 'Usuario o contraseña erroneo')
    
    return render(request, 'users/login.html', {

    })


def logout_view(request):
    
    logout(request)
    messages.success(request, 'Sesion cerrada de manera correcta')
    return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = Registerform(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username =form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        rut = form.cleaned_data.get('rut')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'usuario registrado de manera exitosa')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form' : form
    })