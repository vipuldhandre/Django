from django.db import models

class Lecturer(models.Model):
    lname=models.CharField(max_length=30)
    ledu=models.CharField(max_length=30)
    lfac=models.CharField(max_length=30)
    ldoj=models.DateField()

    def __str__(self):
        return self.lname

class Professor(models.Model):
    pname=models.CharField(max_length=30)
    pedu=models.CharField(max_length=30)
    pfac=models.CharField(max_length=30)
    pdoj=models.DateField()

    def __str__(self):
        return self.pname


# Create your models here.
