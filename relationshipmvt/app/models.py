from django.db import models

class Company(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(self):
        return self.cname


class Languages(models.Model):
    lname=models.CharField(max_length=30)

    def __str__(self):
        return self.lname



class Programmer(models.Model):
    pname=models.CharField(max_length=30)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    language=models.ManyToManyField(Languages)

    def __str__(self):
        return self.pname

# Create your models here.
