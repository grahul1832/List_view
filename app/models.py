from django.db import models


# Create your models here.
class Trainer(models.Model):
    t_name=models.CharField(max_length=100,primary_key=True)
    subject=models.CharField(max_length=100)
    age=models.IntegerField()
