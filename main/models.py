from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name