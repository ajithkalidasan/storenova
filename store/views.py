from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Category
from . import forms


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


def register_user(request):
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("home")
        else:
            messages.success(request, "Registration Failed")
            return redirect("register")

    else:
        return render(request, "store/register.html", {"form": form})
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = forms.UpdateUserForm(request.POST or None,instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Profile Updated")
            return redirect("home")
        
    
        return render(request, "store/update_user.html", {"user_form": user_form})
    else:
        messages.error(request, "Login Required")
        return redirect("login")
    

def product(request,pk):

    product = Product.objects.get(id= pk)
    return render(request, "store/product.html", {"product": product})

def category(request,foo):
    # Replace hyphen with space
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        context = {"category": category, "products": products}
        return render(request, "store/category.html", context)
    except:
        messages.error(request, "Category does not exist")
        return redirect("home")
    
def category_summary(request):
    categories  = Category.objects.all()
    
    context = {"categories": categories}
    return render(request, "store/category_summary.html", context)