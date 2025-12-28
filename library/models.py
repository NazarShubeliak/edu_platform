from django.db import models
from django.conf import settings

class LibraryItem(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    file = models.FileField(upload_to="library_book/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="upload_books"
    )
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
