from django.db import models
from Clients.models import Client
from Departments.models import Department
from clientele.utils import EVENT_STATUS_CHOICES

class Event(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=EVENT_STATUS_CHOICES, default=1)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    info = models.TextField()

    def __str__(self):
        return "%s" % (self.id)
