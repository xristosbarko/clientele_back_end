from django.urls import path
from rest_framework.authtoken import views

app_name = 'auth'

urlpatterns = [
	path('login', views.obtain_auth_token)
]