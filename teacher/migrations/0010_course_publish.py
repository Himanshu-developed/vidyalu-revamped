# Generated by Django 3.2.5 on 2021-09-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_course_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]