from django.db import models

# Create your models here.

class hod_table(models.Model):
    REGNAME = models.CharField(max_length=20, unique=True)
    NAME = models.CharField(max_length=100)
    DEPARTMENT = models.CharField(max_length=200,null=True)
    AGE = models.IntegerField(default=0)
    DOB = models.DateField()
    MAIL = models.CharField(max_length=100)
    PHONE = models.BigIntegerField(default=0)
    PROFILE = models.ImageField(default='user.png', upload_to='images', null=True, blank=True)
