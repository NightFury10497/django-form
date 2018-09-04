# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    male = "Male"
    female = "Female"
    gender_choices = ((male,"Male"),(female,"Female"))
    name = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField()
    surname = models.CharField(max_length=128, null=True, blank=True)
    section = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=30,
                                      choices=gender_choices
                                      )

