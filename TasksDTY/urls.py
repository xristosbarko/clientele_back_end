from django.urls import path
from .views import TaskDTYList, TaskDTYDetails, TaskDTYCreate, TaskDTYEdit, TaskDTYDelete, TaskDTYInputElementSearchList

app_name = 'tasksDTY'

urlpatterns = [
	path('', TaskDTYList.as_view()),
	path('get/<pk>', TaskDTYDetails.as_view()),
	path('create', TaskDTYCreate.as_view()),
	path('edit/<pk>', TaskDTYEdit.as_view()),
	path('delete/<pk>', TaskDTYDelete.as_view()),
	path('taskDTYInputElementSearch/', TaskDTYInputElementSearchList.as_view()),
]