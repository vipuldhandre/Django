from django.db import models

class Born(models.Model):
    bname=models.CharField(max_length=30)
    bdate=models.DateField()
    bcity=models.CharField(max_length=30)

    def __str__(self):
        return self.bname

class Human(models.Model):
    hname=models.CharField(max_length=30)
    htype=models.CharField(max_length=30)
    hcity=models.CharField(max_length=30)
    haddr=models.CharField(max_length=60)

    def __str__(self):
        return self.hname

# Create your models here.
