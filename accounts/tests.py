from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountTest(TestCase):
    def setUp(self):
        # Створення користувачів з різними ролями
        self.admin = User.objects.create_user(username="admin", password="admin1234", role="admin")
        self.teacher = User.objects.create_user(username="New Teacher", password="asdfcehjd", role="teahcer")
        self.student = User.objects.create_user(username="New Student", password="stdunerhkdk", role="student")

    def test_login_succes(self):
        response = self.client.post(reverse("login"), {
            "username": self.teacher.username,
            "password": self.teacher.password
        })

        self.assertEqual(response.status_code, 302)

    def test_login_fail(self):
        response = self.client.post(reverse("login"), {
            "username": self.student.username,
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)

    def test_reqister_by_admin(self):
        self.client.login(usename=self.admin.username, password=self.admin.password)
        response = self.client.post(reverse("register"), {
            "username": "Bob",
            "email": "test@gmail.com",
            "password": "pass1234",
            "role": "student"
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="Bob").exists())

    def test_reqister_by_student(self):
        self.client.login(username=self.student.username, password=self.student.password)
        response = self.client.get(reverse("register"))
        
        self.assertEqual(response.status_code, 302)