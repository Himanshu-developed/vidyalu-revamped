# Generated by Django 3.2.5 on 2021-12-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidyalu_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryMessageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='NAME', max_length=500)),
                ('email', models.EmailField(default='querymail@mail.com', max_length=254)),
                ('number', models.CharField(default='0000000000', max_length=100)),
                ('message', models.TextField(default='Query message')),
            ],
        ),
    ]
