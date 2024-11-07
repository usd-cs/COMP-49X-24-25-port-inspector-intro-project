from django.urls import path
from . import views

urlpatterns = [
    path('intro_app/', views.members, name='intro_app'),
]