from .models import Task
from .serializers import (TaskListSerializer, TaskCreateSerializer,
							TaskUpdateSerializer, TaskDetailsSerializer,
							Choice, ChoiceSerializer)
from rest_framework import generics, filters
from django.http import HttpResponse
from django.views.generic import View
from clientele.utils import render_to_pdf
from clientele.settings import BASE_DIR
from rest_framework.views import APIView
from clientele.utils import TASK_STATUS_CHOICES
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .filters import TaskListFilter

# TASK
class TaskList(generics.ListAPIView):
	"""
	Returns a list of all the Tasks.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskListSerializer
	filter_backends = [TaskListFilter]

class TaskDetails(generics.RetrieveAPIView):
	"""
	Edit a Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskDetailsSerializer

class TaskCreate(generics.CreateAPIView):
	"""
	Add a Task.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TaskCreateSerializer

class TaskEdit(generics.UpdateAPIView):
	"""
	Edit a Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskUpdateSerializer

class TaskDelete(generics.DestroyAPIView):
	"""
	Delete a Task.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskDetailsSerializer

# PDF
class PDF(View):
	def get(self, request, *args, **kwargs):
		task_id = self.kwargs.get("pk")
		task = Task.objects.get(id=task_id)
		task = {
			'task_id': task.id,
			'last_name': task.client_id.last_name,
			'first_name': task.client_id.first_name,
			'phone_number': task.client_id.phone_numbers.last,
			'report_damage': task.report_damage,
			'status': task.status,
			'BASE_DIR': BASE_DIR,
			'date_assignment': task.date_assignment,
			'tech_diagnosis': task.tech_diagnosis,
			'last_briefing': task.briefings.last,
			'date_completion': task.date_completion,
			'spare_parts': task.spare_parts.split("\n"),
			'spare_parts_cost': task.spare_parts_cost,
			'task_cost': task.task_cost,
			'total_cost': float(task.spare_parts_cost) + float(task.task_cost),
			'tech_id': task.tech_id,
		}
		pdf = render_to_pdf('task_pdf.html', task)
		return HttpResponse(pdf, content_type='application/pdf')


# CHOICES
class Choices(APIView):
	"""
	Returns a list of all the Status Choices.
	"""
	permission_classes = [IsAuthenticated]

	def get(self, request):
		choices = [Choice(id=choice[0], name=choice[1]) for choice in TASK_STATUS_CHOICES]
		serializer = ChoiceSerializer(choices, many=True)
		return Response(serializer.data)