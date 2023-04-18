# Generated by Django 3.2.5 on 2021-12-09 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(default='bank name', max_length=500)),
                ('branch_name', models.CharField(default='branch name', max_length=500)),
                ('account_holder_name', models.CharField(default='account holder name', max_length=600)),
                ('account_number', models.IntegerField(default=0)),
                ('ifsc_code', models.CharField(default='ifsc code', max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bank_account_details',
            },
        ),
    ]
