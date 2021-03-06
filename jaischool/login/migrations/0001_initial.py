# Generated by Django 3.1.4 on 2021-01-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('NAME', models.CharField(max_length=20)),
                ('EMAIL', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('AGE', models.IntegerField()),
                ('PHONE_NUMBER', models.BigIntegerField()),
                ('ADDRESS', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_hod', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
