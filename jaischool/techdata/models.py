from django.db import models

# Create your models here.

class teacher_table(models.Model):
    REGNAME = models.CharField(max_length=20, unique=True)
    NAME = models.CharField(max_length=100)
    AGE = models.IntegerField(default=0)
    DOB = models.DateField()
    MAIL = models.CharField(max_length=100)
    PHONE = models.BigIntegerField(default=0)
    HOD_ID = models.CharField(max_length=100,null=True)
    PROFILE = models.ImageField(default='user.png', upload_to='images', null=True, blank=True)
