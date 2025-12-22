from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# from django.http.response import HttpResponse
from .models import StudentProfile, User
from .forms import UserCrateForm

@login_required
def reqister_user(request):
    if request.user.role not in ["admin", "teacher"]:
        return redirect("home")
    
    if request.method == "POST":
        form = UserCrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCrateForm()
    
    return render(request, "accounts/register.html", {"form": form})

@login_required
def delete_student(request, pk):
    if request.user.role not in ["admin", "teacher"]:
        return redirect("home")

    student = get_object_or_404(StudentProfile, pk=pk)
    student.delete()
    return redirect("students_list")

@login_required
def edit_student(request, pk):
    if request.user.role != "admin":
        return redirect("home")

    user = get_object_or_404(User, id=pk)

    if request.method == "POST": 
        user.username = request.POST.get("username") 
        password = request.POST.get("password") 
        if password: # якщо пароль введено 
            user.password = make_password(password) 
        user.save() 
        return redirect("students_list") 
    return render(request, "accounts/edit_student.html", {"user": user})












