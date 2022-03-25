from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mains.as_view(), name='main'),
]