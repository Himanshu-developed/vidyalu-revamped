# Generated by Django 3.2.5 on 2021-11-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0016_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
