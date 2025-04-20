from django.db import models
from odyssey_api.enums import TaskStatus
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField (max_length=50,
                               choices=TaskStatus.choices,
                               default=TaskStatus.NEW)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(timezone.now)
    updated_at = models.DateTimeField(timezone.now)

