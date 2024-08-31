from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_summary, name="cart_details"),
    path("add/", views.cart_add, name="cart_add"),
    path("update/", views.cart_update, name="cart_update"),
    path("checkout/", views.cart_checkout, name="cart_checkout"),
    path(("remove/<int:product_id>/"), views.cart_remove, name="cart_remove"),

]
