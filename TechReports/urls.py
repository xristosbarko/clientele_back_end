from django.urls import path
from .views import TechReportList, TechReportDetails, TechReportCreate, TechReportEdit, TechReportDelete

app_name = 'techReports'

urlpatterns = [
	path('', TechReportList.as_view()),
	path('get/<pk>', TechReportDetails.as_view()),
	path('create', TechReportCreate.as_view()),
	path('edit/<pk>', TechReportEdit.as_view()),
	path('delete/<pk>', TechReportDelete.as_view()),
]