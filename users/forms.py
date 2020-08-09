from django import forms
from django.db import models
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class UserRegiserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password']