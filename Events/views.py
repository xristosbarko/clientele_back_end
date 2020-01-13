from .models import Event
from .serializers import EventListSerializer, EventCreateSerializer, EventUpdateDetailsSerializer, Choice, ChoiceSerializer, CalendarSerializer
from rest_framework import generics, filters
from rest_framework.views import APIView
from clientele.utils import EVENT_STATUS_CHOICES
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .filters import EventListFilter

class EventList(generics.ListAPIView):
	"""
	Returns a list of all the Events.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Event.objects.all()
	serializer_class = EventListSerializer
	filter_backends = [EventListFilter]

class EventDetails(generics.RetrieveAPIView):
	"""
	Edit an Event.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Event.objects.all()
	serializer_class = EventUpdateDetailsSerializer

class EventCreate(generics.CreateAPIView):
	"""
	Add an Event.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = EventCreateSerializer

class EventEdit(generics.UpdateAPIView):
	"""
	Edit an Event.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Event.objects.all()
	serializer_class = EventUpdateDetailsSerializer

class EventDelete(generics.DestroyAPIView):
	"""
	Delete an Event.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Event.objects.all()
	serializer_class = EventUpdateDetailsSerializer

# CHOICES
class Choices(APIView):
	"""
	Returns a list of all the Status Choices.
	"""
	permission_classes = [IsAuthenticated]

	def get(self, request):
		choices = [Choice(id=choice[0], name=choice[1]) for choice in EVENT_STATUS_CHOICES]
		serializer = ChoiceSerializer(choices, many=True)
		return Response(serializer.data)

class CalendarList(generics.ListAPIView):
	"""
	Returns a list of all the Events.
	"""
	permission_classes = [IsAuthenticated]
	pagination_class = None
	queryset = Event.objects.all()
	serializer_class = CalendarSerializer