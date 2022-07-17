from django.db import models
from django.conf import settings
from django.urls import reverse

class Student(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    levels = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    # student_name = models.IntegerField()
    mat_no = models.CharField(max_length=15, unique=True)
    student_gender = models.CharField(max_length=8,null=True, choices=select_gender)
    student_class_name = models.CharField(max_length=8,null=True)
    student_level = models.CharField(max_length=8,null=True, choices=levels)
    student_date_of_birth = models.DateField(null=True)
    active = models.BooleanField(max_length=1, default=0)
    student_reg = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.mat_no