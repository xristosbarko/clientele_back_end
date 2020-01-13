from django.db import models
from Clients.models import Client
from Techs.models import Tech
from Devices.models import Device
from clientele.utils import TASK_STATUS_CHOICES

class Task(models.Model):
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_assignment = models.DateTimeField(auto_now_add=True)
	report_damage = models.TextField()
	type_of_device = models.ForeignKey(Device, on_delete=models.SET_NULL, blank=True, null=True)
	tech_id = models.ForeignKey(Tech, on_delete=models.CASCADE)
	tech_diagnosis = models.TextField(blank=True)
	status = models.CharField(max_length=1, choices=TASK_STATUS_CHOICES, default=1)
	date_completion = models.DateTimeField(null=True)
	ip = models.CharField(max_length=15, blank=True)
	spare_parts = models.TextField(blank=True)
	spare_parts_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
	task_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
	observations = models.TextField(blank=True)

	def __str__(self):
		return "%s" % (self.id)


class Briefing(models.Model):
	task_id = models.ForeignKey(Task, related_name='briefings', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s" % (self.date)