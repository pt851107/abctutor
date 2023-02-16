from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='summercamp'),
    path('<int:camp_id>', views.camp_detail, name='camp_detail') 
]
