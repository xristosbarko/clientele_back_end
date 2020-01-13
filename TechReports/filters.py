from rest_framework.filters import BaseFilterBackend
import coreapi
from clientele.utils import set_if_not_none
from .models import TechReport

class TechReportListFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['client', 'department', 'ip', 'type_of_device', 'sent', 'date_from', 'date_to']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters

	def filter_queryset(self, request, queryset, view):
		parameters = {}

		client = request.query_params.get('client', None)
		department = request.query_params.get('department', None)
		ip = request.query_params.get('ip', None)
		type_of_device = request.query_params.get('type_of_device', None)
		sent = request.query_params.get('sent', None)
		date_from = request.query_params.get('date_from', None)
		date_to = request.query_params.get('date_to', None)

		if client:
			client = client.strip().replace(" ", "").lower()

		if sent:
			choices = [None, True, False]
			sent = choices[int(sent)]

		set_if_not_none(parameters, "task_dty_id__client_id__slug", client)
		set_if_not_none(parameters, "task_dty_id__department_id__name", department)
		set_if_not_none(parameters, "ip", ip)
		set_if_not_none(parameters, "type_of_device__id", type_of_device)
		set_if_not_none(parameters, "sent", sent)
		set_if_not_none(parameters, "date__gte", date_from)
		set_if_not_none(parameters, "date__lte", date_to)

		queryset = TechReport.objects.filter(**parameters)
		return queryset