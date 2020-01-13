from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

class DepartmentList(generics.ListAPIView):
	"""
	Returns a list of all the Departments.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class DepartmentDetails(generics.RetrieveAPIView):
	"""
	Edit a Departments.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	lookup_field = 'name'

class DepartmentCreate(generics.CreateAPIView):
	"""
	Add a Department.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = DepartmentSerializer

class DepartmentEdit(generics.UpdateAPIView):
	"""
	Edit a Department.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer

class DepartmentDelete(generics.DestroyAPIView):
	"""
	Delete a Department.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer