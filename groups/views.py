from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Group, Department, DepartmentFile, GroupFile
from accounts.models import StudentProfile

User = get_user_model()

# Create your views here.
@login_required
def create_group(request):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    if request.method == "POST":
        name = request.POST.get("name")
        group = Group.objects.create(name=name)
        return redirect("group_list")

    return render(request, "groups/create_group.html")

@login_required
def delete_group(request, pk):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    group = get_object_or_404(Group, id=pk)
    group.delete()
    return redirect("group_list")


@login_required
def group_list(request):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    groups = Group.objects.all()
    return render(request, "groups/group_list.html", {"groups": groups})

@login_required
def group_detail(request, pk):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    group = get_object_or_404(Group, pk=pk)
    students = group.students.all()
    # students = User.objects.filter(groups=group)

    if request.method == "POST":
        action = request.POST.get("action")
        student_profile_id = request.POST.get("student_id")
        student = get_object_or_404(StudentProfile, pk=student_profile_id)
        
        if action == "add":
            group.students.add(student)
        elif action == "remove":
            group.students.remove(student)

        return redirect("group_detail", pk=group.pk)

    available_students = StudentProfile.objects.filter(group__isnull=True)

    return render(request, "groups/group_detail.html", {
        "group": group,
        "students": students,
        "available_students": available_students
    })

@login_required
def department_list(request):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    departments = Department.objects.all()
    return render(request, "groups/department_list.html", {"departments": departments})


@login_required
def create_department(request):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        Department.objects.create(name=name, description=description, created_by=request.user)

        return redirect("department_list")

    return render(request, "groups/create_department.html")

@login_required
def department_edit(request, pk):
    if request.user.role not in ["teacher", "admin"]:
        redirect("home")

    department = get_object_or_404(Department, pk=pk)
    # groups = Group.objects.all()
    availbable_groups = Group.objects.exclude(department=department)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        if name:  # тільки якщо є
            department.name = name
        if description is not None:
            department.description = description
        department.save()

        selected_groups = request.POST.getlist("groups")
        department.groups.set(Group.objects.filter(id__in=selected_groups))

        return redirect("department_list")

    return render(request, "groups/department_edit.html", {
        "department": department,
        "availbable_groups": availbable_groups 
    })

@login_required
def upload_file(request):
    # доступ лише для викладача або адміна
    if request.user.role not in ["teacher", "admin"]:
        return redirect("home")

    departments = Department.objects.all()
    groups = Group.objects.all()

    if request.method == "POST":
        target_type = request.POST.get("target_type")  # "department" або "group"
        file = request.FILES.get("file")

        if target_type == "department":
            department_id = request.POST.get("department_id")
            department = get_object_or_404(Department, pk=department_id)
            DepartmentFile.objects.create(
                department=department,
                uploaded_by=request.user,
                file=file
            )

        elif target_type == "group":
            group_id = request.POST.get("group_id")
            group = get_object_or_404(Group, pk=group_id)
            GroupFile.objects.create(
                group=group,
                uploaded_by=request.user,
                file=file
            )

        return redirect("home")  # після завантаження можна редіректнути куди треба

    return render(request, "groups/upload_file.html", {
        "departments": departments,
        "groups": groups,
    })

