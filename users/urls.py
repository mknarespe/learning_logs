"""Визначити регулярні вирази URL"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
	#Додати уставні UEL auth (автентифікації)
	path('', include('django.contrib.auth.urls')),
	#Сторінка реєстрації
	path('register/', views.register, name='register'),
]