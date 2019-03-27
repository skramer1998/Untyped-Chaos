# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import MyModel
admin.site.register(MyModel)
