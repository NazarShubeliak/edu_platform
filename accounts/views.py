from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import UserCrateForm

@login_required
def reqister_user(request):
    if request.user.role not in ["amdin", "teacher"]:
        return HttpResponse(status=400)
    
    if request.method == "POST":
        form = UserCrateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
    else:
        form = UserCrateForm()
    
    return render(request, "accounts/reqister.html", {"form": form})