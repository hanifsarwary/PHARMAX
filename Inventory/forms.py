from django.forms import ModelForm
from django import forms
from User.models import CustomUser,Branch


class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(ModelForm):
    password =forms.CharField(widget=forms.PasswordInput)
    bid = forms.ModelChoiceField(queryset=Branch.objects.all())
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','dob','password','phone','salary','cnic','bid','address']

        widgets = {
            'dob': DateInput()
        }
