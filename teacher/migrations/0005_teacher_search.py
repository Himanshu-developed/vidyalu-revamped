# Generated by Django 3.2.5 on 2021-08-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_teacher_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='search',
            field=models.CharField(blank=True, max_length=199, null=True),
        ),
    ]
