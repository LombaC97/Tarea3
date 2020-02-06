from django.urls import path

from . import views

app_name='login'

urlpatterns = [


	path('',views.index, name='index'),
	path('register/', views.register, name='register'),
	path('register_usuario/', views.register_usuario, name='register_usuario'),
	path('home/', views.autentificar, name='autentificar'),
	path('home/<str:correo>/',views.home, name='home'),




]