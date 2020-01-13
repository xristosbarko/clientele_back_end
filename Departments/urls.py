from django.urls import path
from .views import DepartmentList, DepartmentDetails, DepartmentCreate, DepartmentEdit, DepartmentDelete

app_name = 'departments'

urlpatterns = [
	path('', DepartmentList.as_view()),
	path('get/<name>', DepartmentDetails.as_view()),
	path('create', DepartmentCreate.as_view()),
	path('edit/<pk>', DepartmentEdit.as_view()),
	path('delete/<pk>', DepartmentDelete.as_view()),
]