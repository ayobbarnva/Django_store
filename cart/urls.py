from django.urls import path
from . import views
urlpatterns=[
    path('cart/',views.cart_view,name='cart'),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/',views.remove_from_cart,name='remove_cart'),
    path('increase/<int:item_id>',views.increase,name='increase'),
    path('decrease/<int:item_id>',views.decrease,name='decrease')

]