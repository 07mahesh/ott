from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('stored/',views.stored_movies,name='stored'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('details/<int:pk>/',views.view_movie_details,name='details'),
    path('update/<int:pk>/',views.update_movie,name='update'),
    path('delete/<int:pk>/', views.delete_movie,name='delete'),
    path('search_movie/',views.search_movie,name='search_movie'),
    path('register/',views.register_user,name='register'),
    path('login_user/',views.user_login,name='login_user')
]


