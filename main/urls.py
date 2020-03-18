from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('set-ip/', views.set_ip, name = 'set_ip'),	
	path('delete-ip/', views.delete_ip, name = 'delete_ip'),
]