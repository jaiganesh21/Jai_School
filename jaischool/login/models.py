from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.

class accountmanager(BaseUserManager):
    def create_user(self, username, password , NAME = "admin",EMAIL = "admin@gmail.com",DOB = datetime.today().strftime('%Y-%m-%d'), AGE = "20",PHONE_NUMBER = "0123456789",ADDRESS="abcd",is_teacher="True",is_student="True",is_hod="True"):
        if not username:
            raise ValueError("username required")

        user = self.model(
            username = username,
            EMAIL = EMAIL,
            NAME=NAME,
            DOB=DOB,
            AGE=AGE,
            PHONE_NUMBER=PHONE_NUMBER,
            ADDRESS=ADDRESS,
            is_teacher = is_teacher,
            is_student = is_student,
            is_hod = is_hod,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_teacher = True
        user.is_hod = True
        user.is_student = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class account(AbstractBaseUser):

    NAME = models.CharField(max_length=20)
    EMAIL = models.CharField(max_length=30)
    DOB = models.DateField(null=True)
    AGE = models.IntegerField(null=True)
    PHONE_NUMBER = models.BigIntegerField(null=True)
    ADDRESS = models.CharField(max_length=200)
    username = models.CharField(max_length=20, unique=True)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = accountmanager()

    def __str__(self):
        return self.username

    def has_perm(self , perm , obj = None):
        return self.is_admin

    def has_module_perms(self , app_label ):
        return True
