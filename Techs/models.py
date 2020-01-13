from django.db import models

class Tech(models.Model):
	slug = models.CharField(max_length=65, blank=True)
	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=15)

	class Meta:
		unique_together = ['last_name', 'first_name']

	def __str__(self):
		return "%s %s" % (self.last_name, self.first_name)

	def get_full_name(self):
		return "%s %s" % (self.last_name, self.first_name)