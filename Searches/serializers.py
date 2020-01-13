from rest_framework import serializers
from Tasks.models import Task
from TechReports.models import TechReport

class TaskListSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='client_id')

	class Meta:
		model = Task
		fields = (
			'id',
			'date_assignment',
			'client',
			'ip',
			'report_damage',
		)

class TechReportListSerializer(serializers.ModelSerializer):
	client = serializers.CharField(source='task_dty_id.client_id')
	department = serializers.CharField(source='task_dty_id.department_id')
	ip = serializers.CharField(source='task_dty_id.ip')
	
	class Meta:
		model = TechReport
		fields = (
			'id',
			'date',
			'client',
			'department',
			'ip',
			'pdf',
			'generate_pdf',
		)