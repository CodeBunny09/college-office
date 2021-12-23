# Django Modules
from typing import Match
from django.db import models

# Pip Modules
import datetime 

# Custom Modules
from .validators import validate_file_extension


class Course(models.Model):
    coursename = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return self.coursename

    def __str__(self) -> str:
        return self.coursename

class Student(models.Model):
    name = models.CharField(max_length=100)
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_number_or_usn_number = models.CharField(max_length=100, blank=True)
    
    
    age = models.IntegerField(default=0)
    dob = models.DateField(blank=True, default=datetime.date.today())

    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)

    email = models.EmailField(blank=True)
    contact_number_1 = models.BigIntegerField(default=0000000000)
    contact_number_2 = models.BigIntegerField(default=0000000000)

    blood_group = models.CharField(max_length=3, blank=True)

    religion = models.CharField(max_length=100, blank=True)
    caste = models.CharField(max_length=100, blank=True)

    batch = models.DurationField(null=True)
    semester = models.IntegerField(default=0)


    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def get_name(self):
        return self.name

class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    father_email = models.EmailField(blank=True)
    mother_email = models.EmailField(blank=True)

    parent_contact_number_1 = models.IntegerField(default=0000000000)
    parent_contact_number_2 = models.IntegerField(default=0000000000)

    def __repr__(self) -> str:
        return self.student.name + " Parents"

    def __str__(self) -> str:
        return self.student.name + " Parents"

class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class_10_result = models.FileField(upload_to=f"documents/10", validators=[validate_file_extension], blank=True)
    class_12_result = models.FileField(upload_to=f"documents/12", validators=[validate_file_extension], blank=True)

    PAN_Number = models.CharField(max_length=10)
    Adhaar_Number = models.BigIntegerField(default=0000000000000)

    def __repr__(self) -> str:
        return self.student.name + "'s Documents"

    def __str__(self) -> str:
        return self.student.name + "'s Documents"


