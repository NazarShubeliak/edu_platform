from django.urls import path
from django.contrib.auth import views as auth_views
from .views import reqister_user, delete_student, edit_student, student_profile

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("register/", reqister_user, name="register"),
    path("profile/", student_profile, name="profile"),
    path("students/delete/<int:pk>/", delete_student, name="delete_student"),
    path("students/edit/<int:pk>/", edit_student, name="edit_student"),
]
