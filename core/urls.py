from django.urls import path
from .views import home, students_list

urlpatterns = [
    path("", home, name="home"),
    path("students/", students_list, name="students_list"),
]
