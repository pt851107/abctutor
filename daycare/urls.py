from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='daycare'),
    path('<int:id>/<slug:slug>/', views.daycare_detail, name='daycare_detail'),
]
