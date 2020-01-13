from Tasks.models import Task
from TasksDTY.models import TaskDTY
from TechReports.models import TechReport

from .serializers import TaskListSerializer, TechReportListSerializer

from rest_framework.views import APIView
from rest_framework import generics
from clientele.utils import set_if_not_none
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .filters import AdvancedSearchFilter

class AdvancedSearch(APIView):
	"""
	Returns a list of Tasks and Tech Reports based on the query params.
	"""
	filter_backends = [AdvancedSearchFilter]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None, **kwargs):
		taskParameters = {}
		techReportsParameters = {}

		client = self.request.query_params.get('client', None)
		date_from = self.request.query_params.get('date_from', None)
		date_to = self.request.query_params.get('date_to', None)
		department = self.request.query_params.get('department', None)
		ip = self.request.query_params.get('ip', None)

		if client:
			client = client.strip().replace(" ", "").lower()

		set_if_not_none(taskParameters, "client_id__slug", client)
		set_if_not_none(taskParameters, "date_assignment__gte", date_from)
		set_if_not_none(taskParameters, "date_assignment__lte", date_to)

		set_if_not_none(techReportsParameters, "task_dty_id__client_id__slug", client)
		set_if_not_none(techReportsParameters, "task_dty_id__department_id__name", department)
		set_if_not_none(techReportsParameters, "task_dty_id__ip", ip)
		set_if_not_none(techReportsParameters, "date__gte", date_from)
		set_if_not_none(techReportsParameters, "date__lte", date_to)

		if not taskParameters and not techReportsParameters:
			return Response({
				'tasks': [],
				'tech_reports': []
			})

		tasks = Task.objects.filter(**taskParameters)
		tech_reports = TechReport.objects.filter(**techReportsParameters)

		task_serializer = TaskListSerializer(tasks, many=True)
		tech_reports_serializer = TechReportListSerializer(tech_reports, context={'request': request}, many=True)

		return Response({
			'tasks': task_serializer.data,
			'tech_reports': tech_reports_serializer.data
		})