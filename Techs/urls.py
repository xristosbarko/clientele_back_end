from django.urls import path
from .views import TechList, TechDetails, TechCreate, TechEdit, TechDelete

app_name = 'techs'

urlpatterns = [
	path('', TechList.as_view()),
	path('get/<slug>', TechDetails.as_view()),
	path('create', TechCreate.as_view()),
	path('edit/<pk>', TechEdit.as_view()),
	path('delete/<pk>', TechDelete.as_view()),
]