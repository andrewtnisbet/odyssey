from django.db import  models


class TaskStatus(models.TextChoices):
    NEW = 'new', 'New'
    ACTIVE = 'active', 'Active'
    OVERDUE = 'overdue', 'Overdue'
    DONE = 'done', 'Done'
    CANCELLED = 'cancelled', 'Cancelled'