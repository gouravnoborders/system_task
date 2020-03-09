# from __future__ import unicode_literals

from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.IntegerField()

    def __str__(self):
        return self.name