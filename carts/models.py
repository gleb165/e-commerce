from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField('accounts.user', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart #{self.id} - User: {self.user}"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sku = models.ForeignKey('products.sku', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"OrderItem #{self.id} - SKU: {self.sku} - Quantity: {self.quantity}"