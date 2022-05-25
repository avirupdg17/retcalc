from django.urls import path,include
from . import views

app_name = 'usercreation'
urlpatterns = [
    path('signup/',views.register,name='signup'),
    path('login/',views.user_login,name='userlogin'),
    path('',views.index,name='index'),
    path('logout/',views.user_logout,name='logout')
]