from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='szczeg_post'),
    path('post/new', views.post_new, name='post_new'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', views.password_view, name='password'),

]
