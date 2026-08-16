from . import views
from django.urls import path
urlpatterns=[
    path('login/',views.login_views,name='login'),
    path('signup/',views.sigin_views,name='signup'),
    path('logout/',views.logout_views,name='logout'),
    path('edit_profile/',views.edit_account,name='edit'),
    path('profile/',views.show_profile,name='profile')
]