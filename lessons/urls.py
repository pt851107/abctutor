from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.index, name='lessons'),
    path('<int:id>/<slug:slug>/', views.lesson_detail, name='lesson_detail') 
]
