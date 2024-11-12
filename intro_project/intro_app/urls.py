from django.urls import path
from . import views

urlpatterns = [
    path('intro_app/', views.members, name='intro_app'),
    path('new_post/', views.new_post, name='new_post'),
    path('login/', views.login_view, name='login'),
    path('', views.view_posts, name='home')
]