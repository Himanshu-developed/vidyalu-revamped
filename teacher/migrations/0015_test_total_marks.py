# Generated by Django 3.2.5 on 2021-11-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0014_rename_test_id_test_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='total_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]