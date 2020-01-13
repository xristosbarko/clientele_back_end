from django.db import models
from TasksDTY.models import TaskDTY
from Devices.models import Device

class TechReport(models.Model):
	filename = models.CharField(max_length=25)
	date = models.DateField()
	task_dty_id = models.OneToOneField(TaskDTY, related_name="tech_report", on_delete=models.CASCADE)
	type_of_device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True)
	spare_parts = models.TextField(blank=True)
	comment = models.TextField(blank=True)
	text = models.TextField(blank=True)
	generate_pdf = models.BooleanField(default=False)
	pdf = models.FileField(upload_to='techReports/%Y/%m/%d', null=True)
	sent = models.BooleanField(default=False)

	def __str__(self):
		return "%s" % (self.id)
