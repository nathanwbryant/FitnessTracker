from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Metric(models.Model):
    title = models.CharField(max_length=100)
    units = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Readings(models.Model):
    metric = models.ForeignKey(Metric, related_name="score", on_delete=models.CASCADE)
    date = models.DateTimeField()
    quantity = models.FloatField()
    source = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"\n date: {self.date}\n metric: {self.metric}\n quantity: {self.quantity}\n units: {self.metric.units}\n"
    

