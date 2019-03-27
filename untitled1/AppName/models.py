# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)
    color = models.CharField(max_length=7)

class AccountModel(models.Model):
    Role = models.CharField(max_length=12)
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone = models.CharField(max_length=11)
    Address = models.CharField(max_length=30)

class Login(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
