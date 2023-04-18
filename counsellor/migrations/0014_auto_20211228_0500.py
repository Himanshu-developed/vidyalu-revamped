# Generated by Django 3.2.5 on 2021-12-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0013_session_counsellor_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellor',
            name='admin_comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='counsellor',
            name='permission_by_admin',
            field=models.BooleanField(default=None),
        ),
    ]