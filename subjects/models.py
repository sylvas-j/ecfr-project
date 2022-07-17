from django.db import models
from django.urls import reverse
from django.conf import settings

# from student_classes.models import StudentClass

# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    subject_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    subject_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        # return self.subject_code
        return "%s  %s"%(self.subject_name, self.subject_code)
    
    def get_absolute_url(self):
        return reverse('subjects:subject_list')



class SubjectRegistered(models.Model):
    state = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=8,null=True, default='Pending', choices=state)

    def get_absolute_url(self):
        return reverse('subjects:subject_combination_list')

    def __str__(self):
        return '%s Section-%s'%(self.subject, self.student.username)
    
