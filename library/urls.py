from django.urls import path
from django.contrib.auth import views as auth_views
from .views import library_list, upload_book, delete_book

urlpatterns = [
    path("library_list/", library_list, name="library_list"),
    path("upload_book/", upload_book, name="upload_book"),
    path("delete_book/<int:pk>", delete_book, name="delete_book")
]
