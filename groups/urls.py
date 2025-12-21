from django.urls import path
from .views import create_group, group_list, group_detail, department_list, create_department, department_edit

urlpatterns = [
    path("create_group/", create_group, name="create_group"),
    path("create_department/", create_department, name="create_department"),
    path("departments/<int:pk>/", department_edit, name="department_edit"),
    path("departments/", department_list, name="department_list"),
    path("group/<int:pk>/", group_detail, name="group_detail"),
    path("", group_list, name="group_list"),
]
