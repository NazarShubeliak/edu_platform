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

class DepartmentFile(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="files")
    uploaded_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="department_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.department.name})"


class GroupFile(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="files")
    uploaded_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="group_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.group.name})"

