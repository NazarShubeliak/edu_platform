from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import StudentProfile

# Create your views here.
def home(request):
    return render(request, "core/home.html")


@login_required
def students_list(request):
    if request.user.role not in ["teacher", "admin"]:
        return redirect("home")

    students = StudentProfile.objects.all()
    return render(request, "core/student_list.html", {"students": students})
