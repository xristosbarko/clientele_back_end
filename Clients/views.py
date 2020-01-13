from .models import Client
from .serializers import ClientListSerializer, ClientCreateUpdateSerializer, ClientDetailsSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

# CLIENT
class ClientList(generics.ListAPIView):
	"""
	Returns a list of all the Clients.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Client.objects.all()
	serializer_class = ClientListSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['first_name', 'last_name']

class ClientDetails(generics.RetrieveAPIView):
	"""
	Returns the details of a Client.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = ClientDetailsSerializer

	def get_object(self):
		slug = self.kwargs.get("slug").strip().replace(" ", "").lower()
		client = Client.objects.get(slug=slug)
		return client


class ClientCreate(generics.CreateAPIView):
	"""
	Add a Client.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = ClientCreateUpdateSerializer

class ClientEdit(generics.UpdateAPIView):
	"""
	Edit a Client.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Client.objects.all()
	serializer_class = ClientCreateUpdateSerializer

class ClientDelete(generics.DestroyAPIView):
	"""
	Delete a Client.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Client.objects.all()
	serializer_class = ClientDetailsSerializer