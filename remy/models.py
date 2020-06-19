from django.db import models

# Create your models here.
class DataCollection(models.Model):
    data=models.TextField(max_length=500)
