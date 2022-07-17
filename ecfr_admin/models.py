# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


#  THIS IS FROM SCHOLA_COMMENT DB
class Faculties(models.Model):
    # fac_id = models.AutoField(primary_key=True)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=35)
    description = models.TextField()

    def __str__(self):
        return self.name


class Departments(models.Model):
    # dept_id = models.AutoField(primary_key=True)
    fac_id = models.ForeignKey(Faculties, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=35)
    description = models.TextField()
    study_duration = models.IntegerField()

    def __str__(self):
        return self.name
