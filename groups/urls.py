from django.urls import path
from .views import create_group, group_list, group_detail, department_list, create_department, department_edit, delete_group, upload_file

urlpatterns = [
    path("create_group/", create_group, name="create_group"),
    path("create_department/", create_department, name="create_department"),
    path("departments/<int:pk>/", department_edit, name="department_edit"),
    path("departments/", department_list, name="department_list"),
    path("group/<int:pk>/", group_detail, name="group_detail"),
    path("group/delete/<int:pk>/", delete_group, name="group_delete"),
    path("upload_file/", upload_file, name="upload_file"),
    path("", group_list, name="group_list"),
]
