from django.db import models
from Clients.models import Client
from Departments.models import Department

from .validators import validate_file_extension

class TaskDTY(models.Model):
	code_number = models.IntegerField()
	year = models.CharField(max_length=4)
	date = models.DateField()
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	report_damage = models.TextField()
	tech_diagnosis = models.TextField()
	more_info = models.TextField(blank=True)
	ip = models.CharField(max_length=15, blank=True, null=True)
	department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
	without_tech_report = models.BooleanField(default=False)
	scanned_dty = models.FileField(upload_to="scannedDTY/%Y/%m/%d", validators=[validate_file_extension], null=True, blank=True)

	class Meta:
		unique_together = ['code_number', 'year']

	def __str__(self):
		return "%s %s" % (self.code_number, self.year)
