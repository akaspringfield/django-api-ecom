from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartList.as_view(), name="cart_list"),
    path('cart/add/', views.CartAdd.as_view(), name='cart_add'),

]