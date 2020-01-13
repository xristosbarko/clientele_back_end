from django.urls import path
from .views import DeviceList, DeviceDetails, DeviceCreate, DeviceEdit, DeviceDelete, Choices

app_name = 'devices'

urlpatterns = [
	path('', DeviceList.as_view()),
	path('get/<pk>', DeviceDetails.as_view()),
	path('create', DeviceCreate.as_view()),
	path('edit/<pk>', DeviceEdit.as_view()),
	path('delete/<pk>', DeviceDelete.as_view()),
	path('app_choices', Choices.as_view()),
]