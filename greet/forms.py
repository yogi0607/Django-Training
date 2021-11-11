from django.db import models
from django.forms import ModelForm, fields
# from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import PMProfile, DevProfile, User, Ticket

class ManagerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name',
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        manager = PMProfile.objects.create(user=user)
        return user

class DeveloperCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name',
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        developer = DevProfile.objects.create(user=user)
        return user


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status']

# class ManagerProfileForm(ModelForm):
#     class Meta:
#         model = PMProfile
#         fields = '__all__'