from django.urls import path
from . import views

urlpatterns = [
    path('intro_app/', views.members, name='intro_app'),
    path('new_post/', views.new_post, name='new_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.view_posts, name='home')
]