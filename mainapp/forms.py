from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "birth_date", "specification", "phone", "email", "address", "salary"]


class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary"]


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["specification", "block", "time", "language", "group_name", "mentor", "student_qty", "status"]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "date"]