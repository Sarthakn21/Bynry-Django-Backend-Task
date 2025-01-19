from django import forms
from .models import User,ServiceRequest
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details', 'attached_file','status']

class UserServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details','attached_file']  # Exclude 'status'
