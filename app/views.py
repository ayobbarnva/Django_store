from django.shortcuts import render,get_object_or_404
from . import models
def one(request):
    data=models.Product.objects.all()
    return render(request,'index.html',context={'data':data})
# Create your views here.
def product_detail(request,id):
    product=get_object_or_404(models.Product,id=id)
    return render(request,'product_detail.html',context={"product": product})