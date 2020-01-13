from django.urls import path
from .views import AdvancedSearch

app_name = 'searches'

urlpatterns = [
	path('advanced', AdvancedSearch.as_view())
]