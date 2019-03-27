# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)
    color = models.CharField(max_length=7)

class AccountModel(models.Model):
    role = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=30)

class Login(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
