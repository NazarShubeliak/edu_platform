from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import UserCrateForm

@login_required
def reqister_user(request):
    if request.user.role not in ["admin", "teacher"]:
        return redirect("")
    
    if request.method == "POST":
        form = UserCrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCrateForm()
    
    return render(request, "accounts/register.html", {"form": form})
