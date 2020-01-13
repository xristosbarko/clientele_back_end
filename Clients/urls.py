from django.urls import path
from .views import ClientList, ClientDetails, ClientCreate, ClientEdit, ClientDelete

app_name = 'clients'

urlpatterns = [
	path('', ClientList.as_view()),
	path('get/<slug>', ClientDetails.as_view()),
	path('create', ClientCreate.as_view()),
	path('edit/<pk>', ClientEdit.as_view()),
	path('delete/<pk>', ClientDelete.as_view()),
]