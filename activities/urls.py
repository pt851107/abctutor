from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.index, name='activities'),
    path('<int:id>/<slug:slug>/', views.activity_detail, name='activity_detail') 
]
