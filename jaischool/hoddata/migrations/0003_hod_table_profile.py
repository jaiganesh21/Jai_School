# Generated by Django 3.1.4 on 2021-02-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoddata', '0002_auto_20210127_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod_table',
            name='PROFILE',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='images'),
        ),
    ]