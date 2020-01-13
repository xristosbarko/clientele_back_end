from django.db import models
from clientele.utils import DEVICE_APP_CHOICES

class Device(models.Model):
	name = models.CharField(max_length=25)
	app = models.CharField(max_length=1, choices=DEVICE_APP_CHOICES, default=1)

	class Meta:
		unique_together = ['name', 'app']

	def __str__(self):
		return "%s" % (self.name)