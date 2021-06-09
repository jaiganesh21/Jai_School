# Generated by Django 3.1.4 on 2021-01-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGNAME', models.CharField(max_length=20, unique=True)),
                ('NAME', models.CharField(max_length=100)),
                ('CLASS', models.CharField(max_length=200)),
                ('AGE', models.IntegerField(default=0)),
                ('DOB', models.DateField()),
                ('MAIL', models.CharField(max_length=100)),
                ('PHONE', models.BigIntegerField(default=0)),
                ('TEACHER_ID', models.CharField(max_length=100)),
            ],
        ),
    ]
