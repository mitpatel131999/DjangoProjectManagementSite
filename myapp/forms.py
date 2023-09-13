from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms

# Sign Up Form
class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=20)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    company_name=forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'company_name', 
            'password1', 
            'password2', 
            ]
