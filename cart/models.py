from app import models as models_app
from django.db import models
from accouants.models import User
class cart_model(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Cart - {self.user.phone_number}'
class CartItem(models.Model):
    cart=models.ForeignKey(cart_model,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(models_app.Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.product} X {self.quantity}"
    