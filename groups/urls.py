from django.urls import path
from .views import create_group, group_list

urlpatterns = [
    path("create_group/", create_group, name="create_group"),
    path("", group_list, name="group_list"),
]
