# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Word(models.Model):
    id = models.IntegerField(primary_key=True)
    german_word = models.CharField(max_length=250)
    english_translation = models.CharField(max_length=250)
    gender = models.CharField(max_length=4, default="Der")

