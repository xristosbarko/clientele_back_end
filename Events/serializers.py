from rest_framework import serializers
from .models import Event
from Clients.models import Client
from Departments.models import Department

class ClientSerializer(serializers.ModelSerializer):
	full_name = serializers.CharField(source='get_full_name', read_only=True)
	phone_numbers = serializers.SlugRelatedField(slug_field='phone_number', many=True, read_only=True)

	class Meta:
		model = Client
		fields = (
			'full_name',
			'phone_numbers',
		)

class EventListSerializer(serializers.ModelSerializer):
	client = ClientSerializer(source='client_id', read_only=True)

	class Meta:
		model = Event
		fields = (
			'id',
			'client',
			'date',
			'info',
		)

class EventCreateSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	department = serializers.CharField(source='department_id', required=False)

	class Meta:
		model = Event
		fields = (
			'id',
			'client',
			'date',
			'department',
			'info',
		)

	def create(self, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		validated_data["client_id"] = Client.objects.get(slug=client_slug)

		department = validated_data.get('department_id', None)
		if department:
			validated_data["department_id"] = Department.objects.get(name=department)

		event = Event.objects.create(**validated_data)
		return event

class EventUpdateDetailsSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	department = serializers.CharField(source='department_id', required=False)

	class Meta:
		model = Event
		fields = (
			'id',
			'client',
			'date',
			'status',
			'department',
			'info',
		)

	def update(self, instance, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		client = Client.objects.get(slug=client_slug)

		department = validated_data.get('department_id', None)
		if department:
			department = Department.objects.get(name=department)

		instance.client_id = client
		instance.date = validated_data.get('date', "")
		instance.status = validated_data.get('status', "")
		instance.department_id = department
		instance.info = validated_data.get('info', "")

		instance.save()
		return instance

class Choice(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name


class ChoiceSerializer(serializers.Serializer):
	id = serializers.IntegerField(max_value=9)
	name = serializers.CharField(max_length=20)

class CalendarSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='info', read_only=True)
	start = serializers.DateField(source='date', read_only=True)
	end = serializers.DateField(source='date', read_only=True)
	allDay = serializers.BooleanField(default=True, read_only=True)
	client = ClientSerializer(source='client_id', read_only=True)

	class Meta:
		model = Event
		fields = (
			'id',
			'title',
			'start',
			'end',
			'allDay',
			'client',
		)