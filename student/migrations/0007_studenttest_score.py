# Generated by Django 3.2.5 on 2021-11-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studenttest'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttest',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]