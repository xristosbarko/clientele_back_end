from django.db import models

class Department(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return "%s" % (self.name)
