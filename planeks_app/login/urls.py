from django.urls import path
from . import views

urlpatterns = [
    path('', views.logins, name='login'),
]
