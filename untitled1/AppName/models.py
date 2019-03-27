# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)
    color = models.CharField(max_length=7)
