from django.db import models

class Book(models.Model):
    bname=models.CharField(max_length=30)
    bauthor=models.CharField(max_length=30)
    bprice=models.IntegerField()

    def __str__(self):
        return self.bname




# Create your models here.
