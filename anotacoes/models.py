from django.db import models

# Create your models here.

class Note(models.Model):
    index = models.IntegerField()
    note = models.CharField(max_length=255)
    date = models.DateField()
