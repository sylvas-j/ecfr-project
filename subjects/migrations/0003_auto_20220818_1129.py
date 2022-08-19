# Generated by Django 3.2.4 on 2022-08-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20220716_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_level',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_unit',
            field=models.CharField(default=3, max_length=2),
            preserve_default=False,
        ),
    ]
