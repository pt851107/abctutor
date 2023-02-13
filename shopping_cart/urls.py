from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:camp_id>/', views.cart_add, name='cart_add'),
    path('add/<int:lesson_id>/', views.cart_add, name='cart_add'),
    path('add/<int:activity_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:camp_id>/', views.cart_remove, name='cart_remove'),
    path('remove/<int:lesson_id>/', views.cart_remove, name='cart_remove'),
    path('remove/<int:activity_id>/', views.cart_remove, name='cart_remove')
]
