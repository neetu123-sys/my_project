from django import forms
from myapp.models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"



class bookappointmentform(forms.ModelForm):
    class Meta:
        model=bookappointment
        fields="__all__" 
        

User  = get_user_model()

class CustomuserCreationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']        




