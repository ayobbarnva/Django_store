from django.shortcuts import render,redirect,get_object_or_404
from .models import cart_model,CartItem
from app.models import Product

def cart_view(request):
    if request.user.is_authenticated:
        cart,created=cart_model.objects.get_or_create(user=request.user)
        items=cart.items.all()
        return render(request,'cart.html',context={'cart':cart,'items':items})
    else:
        return redirect('/login/')


def add_to_cart(request,product_id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method=='POST':
        cart,created=cart_model.objects.get_or_create(user=request.user)
        product=get_object_or_404(Product,id=product_id)
        item,created=CartItem.objects.get_or_create(cart=cart,product=product)
        if not created:
            item.quantity += 1
            item.save()
        return redirect('cart')
    return redirect('home')
def remove_from_cart(request,item_id):
    item=CartItem.objects.filter(id=item_id,cart__user=request.user).first()
    if item:
        item.delete()
    return redirect('cart')
def increase(request,item_id):
    if request.user.is_authenticated:
        item=CartItem.objects.filter(id=item_id,cart__user=request.user).first()
        if item and item.quantity<item.product.stock:
            item.quantity +=1
            item.save()
        return redirect('cart')
    else:
        return redirect('/login/')
    

def decrease(request,item_id):
    if request.user.is_authenticated:
        item=CartItem.objects.filter(id=item_id,cart__user=request.user).first()
        if item :
            if item.quantity >1:
                item.quantity -=1
                item.save()
            else:
                item.delete()

        return redirect('cart')
      
    else:
       return redirect('/login/')
 