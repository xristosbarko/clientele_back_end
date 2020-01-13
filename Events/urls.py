from django.urls import path
from .views import EventList, EventDetails, EventCreate, EventEdit, EventDelete, Choices, CalendarList

app_name = 'event'

urlpatterns = [
	path('', EventList.as_view()),
	path('get/<pk>', EventDetails.as_view()),
	path('create', EventCreate.as_view()),
	path('edit/<pk>', EventEdit.as_view()),
	path('delete/<pk>', EventDelete.as_view()),
	path('status_choices', Choices.as_view()),
	path('calendar', CalendarList.as_view()),
]