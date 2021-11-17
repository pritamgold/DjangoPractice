from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuName = models.CharField(max_length=70)
    stuEmail = models.EmailField(max_length=70)
    password = models.CharField(max_length=20)
