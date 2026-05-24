from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
