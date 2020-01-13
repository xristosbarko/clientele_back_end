from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskEdit, TaskDelete, PDF, Choices

app_name = 'tasks'

urlpatterns = [
	path('', TaskList.as_view()),
	path('get/<pk>', TaskDetails.as_view()),
	path('create', TaskCreate.as_view()),
	path('edit/<pk>', TaskEdit.as_view()),
	path('delete/<pk>', TaskDelete.as_view()),
	path('pdf/<pk>', PDF.as_view(), name="pdf"),
	path('status_choices', Choices.as_view()),
]