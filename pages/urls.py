from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('daycare', views.daycare, name='daycare'),
    path('infantcare', views.infantcare, name='infantcare'),
    path('summercamp', views.summercamp, name='summercamp'),
    path('lessons', views.lessons, name='lessons'),
    path('activities', views.activities, name='activities'),
    path('contact', views.contact, name='contact'),
    path('teachers', views.teachers, name='teachers'),
]
