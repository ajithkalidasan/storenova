from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.ShippingAdress)

@admin.register(models.ShippingAdress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address1', 'city',  ]
    
