from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "store/index.html", {"products": products})


def about(request):
    return render(request, "about.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect("home")
        else:
            messages.success(request, "Login Failed")
            return redirect("login")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect("home")
