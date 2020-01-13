from rest_framework import serializers
from .models import Task, Briefing
from Clients.models import Client
from Techs.models import Tech
from django.urls import reverse

class ClientSerializer(serializers.ModelSerializer):
	full_name = serializers.CharField(source='get_full_name', read_only=True)
	phone_numbers = serializers.SlugRelatedField(slug_field='phone_number', many=True, read_only=True)

	class Meta:
		model = Client
		fields = (
			'full_name',
			'phone_numbers',
		)


class TaskListSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	pdf = serializers.SerializerMethodField()

	class Meta:
		model = Task
		fields = (
			'id',
			'date_assignment',
			'client',
			'report_damage',
			'pdf',
		)

	def get_pdf(self, task):
		pdf = reverse('tasks:pdf', kwargs={'pk': task.id})
		return self.context.get('request').build_absolute_uri(pdf)


class TaskCreateSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	tech = serializers.CharField(source='tech_id')

	class Meta:
		model = Task
		fields = (
			'id',
			'client',
			'report_damage',
			'type_of_device',
			'observations',
			'tech',
		)

	def create(self, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		validated_data["client_id"] = Client.objects.get(slug=client_slug)

		tech_slug = validated_data["tech_id"].strip().replace(" ", "").lower()
		validated_data["tech_id"] = Tech.objects.get(slug=tech_slug)

		task = Task.objects.create(**validated_data)
		return task


class TaskUpdateSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	tech = serializers.CharField(source='tech_id')
	briefing = serializers.BooleanField(write_only=True)

	class Meta:
		model = Task
		fields = (
			'id',
			'client',
			'report_damage',
			'type_of_device',
			'observations',
			'tech',
			'tech_diagnosis',
			'briefing',
			'status',
			'ip',
			'spare_parts',
			'spare_parts_cost',
			'task_cost',
		)

	def update(self, instance, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		client = Client.objects.get(slug=client_slug)

		tech_slug = validated_data["tech_id"].strip().replace(" ", "").lower()
		tech = Tech.objects.get(slug=tech_slug)

		briefing = validated_data.pop('briefing')
		if briefing:
			Briefing.objects.create(task_id=instance)

		instance.client_id = client
		instance.report_damage = validated_data.get('report_damage', "")
		instance.type_of_device = validated_data["type_of_device"]
		instance.observations = validated_data.get('observations', "")
		instance.tech_id = tech
		instance.tech_diagnosis = validated_data.get('tech_diagnosis', "")
		instance.status = validated_data.get('status', "")
		instance.ip = validated_data.get('ip', "")
		instance.spare_parts = validated_data.get('spare_parts', "")
		instance.spare_parts_cost = validated_data.get('spare_parts_cost', 0)
		instance.task_cost = validated_data.get('task_cost', 0)
		
		instance.save()
		return instance


class TaskDetailsSerializer(serializers.ModelSerializer):
	client = ClientSerializer(source='client_id', read_only=True)
	tech = serializers.CharField(source='tech_id.get_full_name')
	briefings = serializers.SlugRelatedField(slug_field='date', many=True, read_only=True)
	pdf = serializers.SerializerMethodField()

	class Meta:
		model = Task
		fields = (
			'id',
			'client',
			'report_damage',
			'type_of_device',
			'observations',
			'tech',
			'tech_diagnosis',
			'status',
			'ip',
			'spare_parts',
			'spare_parts_cost',
			'task_cost',
			'briefings',
			'pdf',
		)

	def get_pdf(self, task):
		pdf = reverse('tasks:pdf', kwargs={'pk': task.id})
		return self.context.get('request').build_absolute_uri(pdf)


class Choice(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name


class ChoiceSerializer(serializers.Serializer):
	id = serializers.IntegerField(max_value=9)
	name = serializers.CharField(max_length=20)