from django import forms
from hod.models import Hod,HodCourses
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        # exclude = ['password1','password2']
        fields = ['username', 'email','first_name','last_name']


class HodForm(forms.ModelForm):
    class Meta:
        model = Hod
        fields = '__all__'
        exclude = ['hod','hod_reg','active']
        widgets = {
            'mat_no'  :   forms.TextInput(attrs={'class':'form-control'}),
            'hod_gender'  :   forms.Select(attrs={'class':'form-control'}),
            'hod_date_of_birth'  :   forms.DateInput(attrs={'class':'form-control'}),
        }


class HodCoursesForm(forms.ModelForm):
    class Meta:
        model = HodCourses
        fields = '__all__'
        exclude = ['hod_reg']
        widgets = {
            'hod'  :   forms.Select(attrs={'class':'form-control'}),
            'courses'  :   forms.Select(attrs={'class':'form-control'}),
        }

