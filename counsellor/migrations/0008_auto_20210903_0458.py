# Generated by Django 3.2.5 on 2021-09-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0007_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='dates_times',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
