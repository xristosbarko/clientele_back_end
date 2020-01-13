from .models import TechReport
from .serializers import TechReportListSerializer, TechReportDetailsSerializer, TechReportCreateUpdateSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .filters import TechReportListFilter

# TECH REPORT
class TechReportList(generics.ListAPIView):
	"""
	Returns a list of all the Tech Reports.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TechReport.objects.all()
	serializer_class = TechReportListSerializer
	filter_backends = [TechReportListFilter]

class TechReportDetails(generics.RetrieveAPIView):
	"""
	Edit a Tech Report.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TechReport.objects.all()
	serializer_class = TechReportDetailsSerializer

class TechReportCreate(generics.CreateAPIView):
	"""
	Add a Tech Report.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TechReportCreateUpdateSerializer

class TechReportEdit(generics.UpdateAPIView):
	"""
	Edit a Tech Report.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TechReport.objects.all()
	serializer_class = TechReportCreateUpdateSerializer

class TechReportDelete(generics.DestroyAPIView):
	"""
	Delete a Tech Report.
	"""
	permission_classes = [IsAuthenticated]
	queryset = TechReport.objects.all()
	serializer_class = TechReportDetailsSerializer