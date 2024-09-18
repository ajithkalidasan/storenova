from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Category,Profile
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
    return render(request, "store/login.html")


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

def update_password(request):
    """
    Handles the password update process for an authenticated user.

    If the user is authenticated, this view checks the request method. If the request method is POST,
    the password update logic should be implemented (currently represented by `pass`). If the request 
    method is GET, it displays a form to the user to reset their password.

    If the user is not authenticated, they are redirected to the 'update_user' view.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: Renders the 'update_password' template with the reset password form if GET method is used.
        Otherwise, it processes the form submission (when POST logic is added).
        Redirect: Redirects to 'update_user' if the user is not authenticated.
    """
    if request.user.is_authenticated:
        current_user = request.user
        
        if request.method == 'POST':
            # Implement password update logic here
            form = forms.ResetPasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password Updated....,")
                # login(request, current_user)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.warning(request, error)
                
        else:
            form = forms.ResetPasswordForm(current_user)
            return render(request, "store/update_password.html", {"form": form})
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
    except Exception:
        messages.error(request, "Category does not exist")
        return redirect("home")
    
def category_summary(request):
    categories  = Category.objects.all()
    
    context = {"categories": categories}
    return render(request, "store/category_summary.html", context)


def update_info(request):
    if request.user.is_authenticated:
        try:
            # Get the current user's profile
            current_profile = Profile.objects.get(user__id=request.user.id)
        except Profile.DoesNotExist:
            # Handle the case where a Profile does not exist for the user
            current_profile = Profile(user=request.user)
        form = forms.ProfileForm(request.POST or None,instance=current_profile)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Profile Updated")
            return redirect("home")
        else:
            # If the form is not valid, display an error message
            messages.error(request, "Please correct the errors below.")

    
        return render(request, "store/update_info.html", {"form": form})
    else:
        messages.error(request, "Login Required")
        return redirect("login")
    
def search(request):
    
    """Handles product search requests.

    This function processes a POST request to search for products by name or description. 
    If products matching the search criteria are found, they are returned to the search template; 
    otherwise, a message indicating no products were found is displayed.

    Args:
        def update_info(request):
    if request.user.is_authenticated:
        # Get or create the current user's profile
        current_profile, created = Profile.objects.get_or_create(user=request.user)
        
        form = forms.ProfileForm(request.POST or None, instance=current_profile)

        if form.is_valid():
            form.save()

            messages.success(request, "Profile Updated")
            return redirect("home")
        else:
            # If the form is not valid, display an error message
            messages.error(request, "Please correct the errors below.")

        return render(request, "store/update_info.html", {"form": form})
    else:
        messages.error(request, "Login Required")
        return redirect("login")
request: The HTTP request object containing the search data.

    Returns:
        HttpResponse: The rendered search template with search results or an error message.
    """

    if request.method != "POST":
        return render(request, "search.html", {})
    searched = request.POST['searched']
    if searched := Product.objects.filter(
        Q(name__icontains=searched) | Q(description__icontains=searched)
    ):
        return render(request, "search.html", {'searched':searched})
    messages.success(request, "That Product Does Not Exist...Please try Again.")
    return render(request, "search.html", {})