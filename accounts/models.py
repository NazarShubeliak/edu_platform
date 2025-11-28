from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOISE = (
        # "studnet" покаже в базі "Student" покаже на сайті для адміна
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    )
    # Вибираємо роль для користувача для деф буде студент
    role = models.CharField(max_length=20, choices=ROLE_CHOISE, default="student")

    def __str__(self):
        return f"{self.username} ({self.role})"