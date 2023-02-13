from django.urls import path
from . import views

app_name = 'infantcare'

urlpatterns = [
    path('', views.index, name='infantcare'),
    path('<int:id>/<slug:slug>/', views.infantcare_detail,
         name='infantcare_detail'),
]
