from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='lessons'),
    path('<int:lesson_id>', views.lesson_detail, name='lesson_detail') 
]
