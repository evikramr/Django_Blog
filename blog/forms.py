from django import forms
from . models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'Mobile_No', 'Address', 'Landmark', 'City', 'State', 'Country', 'Postal_Code', 'Profile_Image']