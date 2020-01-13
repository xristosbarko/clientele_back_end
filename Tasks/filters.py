from rest_framework.filters import BaseFilterBackend
import coreapi
from clientele.utils import set_if_not_none
from .models import Task

class TaskListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['client', 'ip', 'status', 'tech', 'date_from', 'date_to']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		parameters = {}

		client = request.query_params.get('client', None)
		ip = request.query_params.get('ip', None)
		status = request.query_params.get('status', None)
		tech = request.query_params.get('tech', None)
		date_from = request.query_params.get('date_from', None)
		date_to = request.query_params.get('date_to', None)

		if client:
			client = client.strip().replace(" ", "").lower()
		if tech:
			tech = tech.strip().replace(" ", "").lower()

		set_if_not_none(parameters, "client_id__slug", client)
		set_if_not_none(parameters, "ip", ip)
		set_if_not_none(parameters, "status", status)
		set_if_not_none(parameters, "tech_id__slug", tech)
		set_if_not_none(parameters, "date_assignment__gte", date_from)
		set_if_not_none(parameters, "date_assignment__lte", date_to)

		queryset = Task.objects.filter(**parameters)
		return queryset