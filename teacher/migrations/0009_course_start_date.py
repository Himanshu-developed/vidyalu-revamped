# Generated by Django 3.2.5 on 2021-09-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_auto_20210901_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
