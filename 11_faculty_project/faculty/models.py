from django.db import models
class Faculty(models.Model):
    fid = models.CharField(max_length=20)
    title = models.CharField(max_length=50)   # Professor, Asst Prof
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
