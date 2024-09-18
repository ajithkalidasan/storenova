from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShippingAdress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, )
    email =  models.EmailField(null=True, blank=True)
    address1 = models.CharField(max_length=255, null= True, blank=True)
    address2 = models.CharField(max_length=255, null= True, blank=True)
    city = models.CharField(max_length=255, null= True, blank=True)
    state = models.CharField(max_length=255, null= True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Orders by most recent
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'{self.full_name}, {self.city}'