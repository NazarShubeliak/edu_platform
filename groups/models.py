from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    department = models.ManyToManyField(Department, related_name="groups", blank=True)

    def __str__(self):
        return self.name
