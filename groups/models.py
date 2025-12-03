from django.db import models
from django.conf import settings

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={"role": "student"},
        blank=True,
        related_name="group"
    )

    def clean(self):
        for student in self.students.all():
            if student.group.exclude(pk=self.pk).exists():
                raise ValidationError(f"Студент {student.username} вже знаходиться в іншій групі.")

    def __str__(self):
        return self.name

