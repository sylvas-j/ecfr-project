from django.forms import ModelForm
from django import forms
from .models import Subject, SubjectRegistered

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code':  forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SubjectRegisteredForm(ModelForm):
    class Meta:
        model = SubjectRegistered
        fields = ['student','subject']
        widgets = {
            # 'select_class': forms.Select(
            #     attrs={
            #         'class': 'form-control'
            #         }
            #     ),
            'student':  forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'subject':  forms.Select(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }