from django import forms
from students.models import Student
#from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['student','student_reg','active']
        widgets = {
            #'student__username'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_name'  :   forms.TextInput(attrs={'class':'form-control'}),
            'mat_no'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_email'  :   forms.EmailInput(attrs={'class':'form-control'}),
            'student_gender'  :   forms.Select(attrs={'class':'form-control'}),
            'student_class'  :   forms.Select(attrs={'class':'form-control'}),
            'student_date_of_birth'  :   forms.DateInput(attrs={'class':'form-control'}),
        }


