from django.db import models

# Create your models here.
class Student(models.Model):
    usn          = models.CharField(max_length=20)
    name         = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    cie_marks    = models.IntegerField()
