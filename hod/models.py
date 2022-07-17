from django.db import models
from django.conf import settings
from django.urls import reverse

from subjects.models import Subject


class Hod(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    hod = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    mat_no = models.CharField(max_length=15, unique=True)
    hod_gender = models.CharField(max_length=8,null=True, choices=select_gender)
    hod_gender = models.CharField(max_length=8,null=True, choices=select_gender)
    active = models.BooleanField(max_length=1, default=0)
    hod_reg = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('hod:hod_create')

    def __str__(self):
        return self.mat_no

# Create your models here.
class HodCourses(models.Model):
    # hod_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    hod = models.ForeignKey(Hod, null=True, on_delete=models.SET_NULL)
    courses = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    hod_reg = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('hod:hod_courses')

    def __str__(self):
        return self.hod
