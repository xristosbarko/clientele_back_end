from .models import Tech
from .serializers import TechSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

class TechList(generics.ListAPIView):
	"""
	Returns a list of all the Techs.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Tech.objects.all()
	serializer_class = TechSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['last_name', 'first_name']

class TechDetails(generics.RetrieveAPIView):
	"""
	Returns the details of a Tech.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TechSerializer

	def get_object(self):
		slug = self.kwargs.get("slug").strip().replace(" ", "").lower()
		tech = Tech.objects.get(slug=slug)
		return tech

class TechCreate(generics.CreateAPIView):
	"""
	Add a Tech.
	"""
	permission_classes = [IsAuthenticated]
	serializer_class = TechSerializer

class TechEdit(generics.UpdateAPIView):
	"""
	Edit a Tech.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Tech.objects.all()
	serializer_class = TechSerializer

class TechDelete(generics.DestroyAPIView):
	"""
	Delete a Tech.
	"""
	permission_classes = [IsAuthenticated]
	queryset = Tech.objects.all()
	serializer_class = TechSerializer