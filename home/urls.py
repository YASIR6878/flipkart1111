from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout")
]
