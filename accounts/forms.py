from django import forms
from .models import User

class UserCrateForm(forms.ModelForm):
    # Для того щоб у формі було <input type="password">
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user