from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='activities'),
    path('<int:activity_id>', views.activity_detail, name='activity_detail') 
]
