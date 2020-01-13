from .models import Device
from .serializers import DeviceListSerializer, DeviceSerializer, Choice, ChoiceSerializer
from rest_framework import generics, filters
from rest_framework.views import APIView
from clientele.utils import DEVICE_APP_CHOICES
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# DEVICE
class DeviceList(generics.ListAPIView):
	"""
	Returns a list of all the Devices.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Device.objects.all()
	serializer_class = DeviceListSerializer
	filter_backends = [filters.SearchFilter]
	pagination_class = None
	search_fields = ['app']

class DeviceDetails(generics.RetrieveAPIView):
	"""
	Edit a Device.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer

class DeviceCreate(generics.CreateAPIView):
	"""
	Add a Device.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = DeviceSerializer

class DeviceEdit(generics.UpdateAPIView):
	"""
	Edit a Device.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer

class DeviceDelete(generics.DestroyAPIView):
	"""
	Delete a Device.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer


# CHOICES
class Choices(APIView):
	"""
	Returns a list of all the App Choices.
	"""
	permission_classes = [IsAuthenticated]

	def get(self, request):
		choices = [Choice(id=choice[0], name=choice[1]) for choice in DEVICE_APP_CHOICES]
		serializer = ChoiceSerializer(choices, many=True)
		return Response(serializer.data)