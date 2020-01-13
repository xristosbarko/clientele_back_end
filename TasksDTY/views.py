from .models import TaskDTY
from .serializers import TaskDTYListSerializer, TaskDTYCreateUpdateDetailsSerializer, TaskDTYInputElementSearchSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .filters import TaskDTYListFilter
from clientele.utils import set_if_not_none

class TaskDTYList(generics.ListAPIView):
	"""
	Returns a list of all the DTY Tasks.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TaskDTY.objects.all()
	serializer_class = TaskDTYListSerializer
	filter_backends = [TaskDTYListFilter]

class TaskDTYDetails(generics.RetrieveAPIView):
	"""
	Edit a DTY Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TaskDTY.objects.all()
	serializer_class = TaskDTYCreateUpdateDetailsSerializer

class TaskDTYCreate(generics.CreateAPIView):
	"""
	Add a DTY Task.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TaskDTYCreateUpdateDetailsSerializer

class TaskDTYEdit(generics.UpdateAPIView):
	"""
	Edit a DTY Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TaskDTY.objects.all()
	serializer_class = TaskDTYCreateUpdateDetailsSerializer

class TaskDTYDelete(generics.DestroyAPIView):
	"""
	Delete a DTY Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TaskDTY.objects.all()
	serializer_class = TaskDTYCreateUpdateDetailsSerializer

class TaskDTYInputElementSearchList(generics.ListAPIView):
	"""
	Returns a list of a all DTY Tasks and their clients.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TaskDTYInputElementSearchSerializer

	def get_queryset(self):
		parameters = {}
		code_number = self.request.query_params.get('search', None)
		set_if_not_none(parameters, "code_number", code_number)
		queryset = TaskDTY.objects.filter(**parameters, tech_report__isnull=True, without_tech_report=False)
		return queryset