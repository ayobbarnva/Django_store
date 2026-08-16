from django.urls import path
from . import views
urlpatterns=[
    path('',views.one,name='home'),
    path('home/',views.one,name="home"),
    path('product/<int:id>/',views.product_detail,name='product_detail')
]