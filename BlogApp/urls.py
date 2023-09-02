from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('login',views.Login,name="login"),
    path('register',views.Register,name="register"),
    path('logout',views.Logout_view,name="logout"),
    path('create_vomit',views.create_vomit,name="create_vomit"),
]