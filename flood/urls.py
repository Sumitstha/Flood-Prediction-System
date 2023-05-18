from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
     path('login',views.loginUser,name="login"),
    path('flood',views.predict),
     path('logout',views.logoutUser,name="logout"),
]
