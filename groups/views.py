from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Group

# Create your views here.
def create_group(request):
    if request.user.role not in ["teacher", "admin"]:
        raise PermissionDenied("Ви не маєте права створювання груп")

    if request.method == "POST":
        name = request.POST.get("name")
        group = Group.objects.create(name=name)
        return redirect("group_list")

    return render(request, "groups/create_group.html")

def group_list(request):
    groups = Group.objects.all()
    return render(request, "groups/group_list.html", {"groups": groups})
