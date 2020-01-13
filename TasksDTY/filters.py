from rest_framework.filters import BaseFilterBackend
import coreapi
from clientele.utils import set_if_not_none
from .models import TaskDTY

class TaskDTYListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['client', 'code_number', 'department', 'ip', 'date_from', 'date_to']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		parameters = {}

		client = request.query_params.get('client', None)
		code_number = request.query_params.get('code_number', None)
		department = request.query_params.get('department', None)
		ip = request.query_params.get('ip', None)
		date_from = request.query_params.get('date_from', None)
		date_to = request.query_params.get('date_to', None)

		if client:
			client = client.strip().replace(" ", "").lower()

		set_if_not_none(parameters, "client_id__slug", client)
		set_if_not_none(parameters, "code_number", code_number)
		set_if_not_none(parameters, "department_id__name", department)
		set_if_not_none(parameters, "ip", ip)
		set_if_not_none(parameters, "date__gte", date_from)
		set_if_not_none(parameters, "date__lte", date_to)

		queryset = TaskDTY.objects.filter(**parameters)
		return queryset