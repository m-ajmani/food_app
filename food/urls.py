from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='food-home'),
	path('reviews/', views.reviews, name='food-reviews'),
	path('login/', views.login, name='food-login'),
	path('register/', views.register, name='food-register'),
]
