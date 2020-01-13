from rest_framework.filters import BaseFilterBackend
import coreapi
from clientele.utils import set_if_not_none
from .models import Event

class EventListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['client', 'department', 'status']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		parameters = {}

		client = request.query_params.get('client', None)
		department = request.query_params.get('department', None)
		status = request.query_params.get('status', None)

		if client:
			client = client.strip().replace(" ", "").lower()

		set_if_not_none(parameters, "client_id__slug", client)
		set_if_not_none(parameters, "department_id__name", department)
		set_if_not_none(parameters, "status", status)

		queryset = Event.objects.filter(**parameters)
		return queryset