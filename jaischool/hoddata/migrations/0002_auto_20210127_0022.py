# Generated by Django 3.1.4 on 2021-01-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoddata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod_table',
            name='DEPARTMENT',
            field=models.CharField(max_length=200, null=True),
        ),
    ]