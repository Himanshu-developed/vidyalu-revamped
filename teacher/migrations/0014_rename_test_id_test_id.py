# Generated by Django 3.2.5 on 2021-11-03 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_alter_test_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='test_id',
            new_name='id',
        ),
    ]
