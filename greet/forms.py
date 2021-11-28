from django.db import models
from django import forms
from django.forms import ModelForm, fields
# from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import PMProfile, DevProfile, User, Ticket

class ManagerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(ManagerCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'placeholder': name})

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        manager = PMProfile.objects.create(user=user)
        return user

class DeveloperCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']
        
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name' : 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(DeveloperCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'placeholder': name})

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

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control', 'placeholder': name})

# class ManagerProfileForm(ModelForm):
#     class Meta:
#         model = PMProfile
#         fields = '__all__'