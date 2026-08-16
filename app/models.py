from django.db import models



# category for model one 
class Category(models.Model):
     name = models.CharField(max_length=100, unique=True)
     slug = models.SlugField(max_length=100, unique=True)
     def __str__(self):
          return self.name
# model one 
class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products')
    price=models.DecimalField(max_digits=50,decimal_places=0)
    discount_price=models.DecimalField(max_digits=50,decimal_places=0)
    image=models.ImageField(upload_to='image_orginal',null=True)
    stock=models.PositiveIntegerField()
    description=models.CharField(max_length=500,null=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
