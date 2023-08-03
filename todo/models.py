from django.db import models
from django.utils import timezone

STATUS_CHOICES=[
    ("in","InProgress"),
    ("bl","Blocked"),
    ("co","Completed"),
    ("ca","Cancelled"),
]

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    def __str__(self) -> str:
        return self.title
