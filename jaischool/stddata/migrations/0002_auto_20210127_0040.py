# Generated by Django 3.1.4 on 2021-01-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stddata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_table',
            name='CLASS',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student_table',
            name='TEACHER_ID',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
