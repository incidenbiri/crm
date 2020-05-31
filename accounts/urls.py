from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('register/', views.registerpage, name="register"),
    path('logout/', views.logoutuser, name="logout"),
    path('', views.homepage, name="home"),

    path('user/', views.userpage, name="user-page"),

    path('user/account/', views.accountsettings, name="account"),

    path('products/', views.productpage, name="products"),
    path('customer/<str:pk>/', views.customerpage, name="customer"),


    path('create_order/<str:pk>/', views.createorder, name="create_order"),
    path('update_order/<str:pk>/', views.updateorder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteorder, name="delete_order"),
]
