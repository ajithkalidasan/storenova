from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_editable = [ 'email']
    search_fields = ["first_name", "last_name"]
    list_per_page = 10

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_sale', 'sale_price', 'description']
    list_editable = ['is_sale', 'sale_price', 'description']
    search_fields = ["name"]
    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status']
    list_editable = ['status']
    search_fields = ["customer"]
    list_per_page = 10