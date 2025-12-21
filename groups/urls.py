from django.urls import path
from .views import create_group, group_list, group_detail

urlpatterns = [
    path("create_group/", create_group, name="create_group"),
    path("group/<int:pk>/", group_detail, name="group_detail"),
    path("", group_list, name="group_list"),
]
