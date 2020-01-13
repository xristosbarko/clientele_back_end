from rest_framework import serializers
from .models import TaskDTY
from Clients.models import Client
from Departments.models import Department
from TechReports.models import TechReport

class TechReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = TechReport
		fields = (
			'id',
			'pdf',
		)

class TaskDTYListSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	department = serializers.CharField(source='department_id')

	class Meta:
		model = TaskDTY
		fields = (
			'id',
			'code_number',
			'date',
			'client',
			'department',
			'report_damage',
			'scanned_dty',
		)

class TaskDTYCreateUpdateDetailsSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')
	department = serializers.CharField(source='department_id')
	tech_report = TechReportSerializer(read_only=True)

	class Meta:
		model = TaskDTY
		fields = (
			'id',
			'client',
			'code_number',
			# 'year',
			'date',
			'report_damage',
			'tech_diagnosis',
			'more_info',
			'ip',
			'department',
			'without_tech_report',
			'scanned_dty',
			'tech_report',
		)

	def create(self, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		validated_data["client_id"] = Client.objects.get(slug=client_slug)

		validated_data["department_id"] = Department.objects.get(name=validated_data["department_id"])

		# validated_data["year"] = validated_data["date"].year

		task_dty = TaskDTY.objects.create(**validated_data)
		return task_dty

	def update(self, instance, validated_data):
		client_slug = validated_data["client_id"].strip().replace(" ", "").lower()
		client = Client.objects.get(slug=client_slug)

		department = Department.objects.get(name=validated_data["department_id"])

		# year = validated_data["date"].year

		instance.client_id = client
		instance.code_number = validated_data.get('code_number', "")
		# instance.year = year
		instance.date = validated_data.get('date', "")
		instance.report_damage = validated_data.get('report_damage', "")
		instance.tech_diagnosis = validated_data.get('tech_diagnosis', "")
		instance.more_info = validated_data.get('more_info', "")
		instance.ip = validated_data.get('ip', "")
		instance.department_id = department
		instance.without_tech_report = validated_data.get('without_tech_report', False)
		instance.scanned_dty = validated_data.get('scanned_dty', instance.scanned_dty)
		
		instance.save()
		return instance

# TaskDTY InputElement Search
class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = (
			'last_name',
			'first_name',
		)

class TaskDTYInputElementSearchSerializer(serializers.ModelSerializer):
	client = ClientSerializer(source="client_id")

	class Meta:
		model = TaskDTY
		fields = (
			'id',
			'code_number',
			'date',
			'client',
		)