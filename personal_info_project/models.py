from django.db import models

from personal_info_project.constants import GENDER_OPTIONS


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS, default='U')

    def __str__(self):
        return self.name