from django.db import models

class University(models.Model):
    uname=models.CharField(max_length=60)

    def __str__(self):
        return self.uname

class College(models.Model):
    cname=models.CharField(max_length=60)

    def __str__(self):
        return self.cname

class Department(models.Model):
    dname=models.CharField(max_length=30)
    university=models.ForeignKey(University,on_delete=models.CASCADE)
    college = models.ManyToManyField(College)

    def __str__(self):
        return self.dname

# Create your models here.
