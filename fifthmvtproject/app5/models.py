from django.db import models

class Tester(models.Model):
    tname=models.CharField(max_length=30)
    tdes=models.CharField(max_length=30)
    tproject=models.CharField(max_length=30)
    tdoj=models.DateField()

    def __str__(self):
        return self.tname

class Developer(models.Model):
    dname=models.CharField(max_length=30)
    ddes=models.CharField(max_length=30)
    dproject=models.CharField(max_length=30)
    ddoj=models.DateField()

    def __str__(self):
        return self.dname

# Create your models here.
