from django.db import models

class Book(models.Model):
    bname=models.CharField(max_length=20)
    bprice=models.IntegerField()
    bauthor=models.CharField(max_length=30)

    def __str__(self):
        return self.bname

class Mobile(models.Model):
    mname=models.CharField(max_length=20)
    mmodel=models.CharField(max_length=20)
    mprice=models.IntegerField()

    def __str__(self):
        return self.mname

# Create your models here.
