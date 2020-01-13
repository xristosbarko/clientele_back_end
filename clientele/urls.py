from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .appConfig import APP_NAME
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include_docs_urls(title=APP_NAME, description='v1.0', public=True)),
	path('auth/', include("Auth.urls")),
	path('clients/', include("Clients.urls")),
	path('departments/', include("Departments.urls")),
	path('techs/', include("Techs.urls")),
	path('tasksDTY/', include("TasksDTY.urls")),
	path('events/', include("Events.urls")),
	path('tasks/', include("Tasks.urls")),
	path('techReports/', include("TechReports.urls")),
	path('devices/', include("Devices.urls")),
	path('searches/', include("Searches.urls")),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)