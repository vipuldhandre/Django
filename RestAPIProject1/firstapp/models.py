from django.db import models


class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    eadd = models.CharField(max_length=30)
# Create your models here.
