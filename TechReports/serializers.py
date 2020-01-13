from rest_framework import serializers
from .models import TechReport
from TasksDTY.models import TaskDTY
from .pdf import GeneratePdf

class TaskDTYSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskDTY
		fields = (
			'id',
			'code_number',
			'year',
		)

class TechReportListSerializer(serializers.ModelSerializer):
	task_dty = TaskDTYSerializer(source='task_dty_id')
	client = serializers.CharField(source='task_dty_id.client_id')
	department = serializers.CharField(source='task_dty_id.department_id')
	type_of_device = serializers.StringRelatedField()
	
	class Meta:
		model = TechReport
		fields = (
			'id',
			'client',
			'department',
			'type_of_device',
			'date',
			'task_dty',
			'pdf',
			'sent',
			'generate_pdf',
		)

class TechReportCreateUpdateSerializer(serializers.ModelSerializer):
	task_dty = serializers.CharField(source='task_dty_id')
	ip = serializers.CharField(max_length=15, required=False)
	text = serializers.CharField(max_length=500)

	class Meta:
		model = TechReport
		fields = (
			'id',
			'filename',
			'task_dty',
			'date',
			'ip',
			'type_of_device',
			'spare_parts',
			'comment',
			'text',
			'sent',
			'generate_pdf',
		)

	def create(self, validated_data):
		task_dty = TaskDTY.objects.get(code_number=validated_data["task_dty_id"])

		ip = validated_data.get('ip', "")
		if ip:
			task_dty.ip = validated_data.pop('ip')
			task_dty.save()

		validated_data["task_dty_id"] = task_dty

		tech_report = TechReport.objects.create(**validated_data)

		if validated_data["generate_pdf"]:
			tech_report.generate_pdf = True
			GeneratePdf(tech_report)
			tech_report.save()

		return tech_report

	def update(self, instance, validated_data):
		if self.partial:
			instance.sent = validated_data.get('sent', False)
			instance.save()
			return instance

		if instance.generate_pdf:
			return instance

		task_dty = TaskDTY.objects.get(code_number=validated_data["task_dty_id"])

		ip = validated_data.get('ip', "")
		if ip:
			task_dty.ip = validated_data.pop('ip')
			task_dty.save()
		
		instance.filename = validated_data.get('filename', "")
		instance.task_dty_id = task_dty
		instance.date = validated_data.get('date', "")
		instance.type_of_device = validated_data.get('type_of_device', "")
		instance.spare_parts = validated_data.get('spare_parts', "")
		instance.comment = validated_data.get('comment', "")
		instance.text = validated_data.get('text', "")
		
		instance.save()

		if validated_data["generate_pdf"]:
			instance.generate_pdf = True
			GeneratePdf(instance)
			instance.save()

		return instance

class TechReportDetailsSerializer(serializers.ModelSerializer):
	task_dty = serializers.IntegerField(source='task_dty_id.code_number')
	ip = serializers.CharField(source='task_dty_id.ip')
	text = serializers.CharField(max_length=500)

	class Meta:
		model = TechReport
		fields = (
			'id',
			'filename',
			'task_dty',
			'date',
			'ip',
			'type_of_device',
			'spare_parts',
			'comment',
			'text',
			'generate_pdf',
		)