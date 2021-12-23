from typing import Match
from django.db import models
import datetime 

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    dob = models.DateField(blank=True, default=datetime.date.today())

    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)

    email = models.EmailField(blank=True)
    contact_number_1 = models.BigIntegerField(default=0000000000)
    contact_number_2 = models.BigIntegerField(default=0000000000)

    blood_group = models.CharField(max_length=3, blank=True)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    father_email = models.EmailField(blank=True)
    mother_email = models.EmailField(blank=True)

    parent_contact_number_1 = models.IntegerField(default=0000000000)
    parent_contact_number_2 = models.IntegerField(default=0000000000)