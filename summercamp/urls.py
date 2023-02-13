from django.urls import path
from . import views

app_name = 'summercamp'

urlpatterns = [
    path('', views.index, name='summercamp'),
    path('<int:id>/<slug:slug>/', views.camp_detail, name='camp_detail') 
]
