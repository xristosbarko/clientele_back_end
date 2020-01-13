from django.db import models

class Client(models.Model):
	slug = models.CharField(max_length=65, blank=True)
	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	city = models.CharField(max_length=30, blank=True)
	address = models.CharField(max_length=30, blank=True)
	fax = models.CharField(max_length=15, blank=True)
	email = models.EmailField(max_length=120, blank=True)
	info = models.TextField(blank=True)
	responsible = models.CharField(max_length=30, blank=True)

	class Meta:
		unique_together = ['last_name', 'first_name']

	def __str__(self):
		return "%s %s" % (self.last_name, self.first_name)

	def get_full_name(self):
		return "%s %s" % (self.last_name, self.first_name)


class Phone(models.Model):
	client_id = models.ForeignKey(Client, related_name='phone_numbers', on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=15, unique=True)

	def __str__(self):
		return "%s" % (self.phone_number)