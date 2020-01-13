from django.db import models


class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=30)
    srn=models.IntegerField()
    sclass=models.CharField(max_length=20)
    sschool=models.CharField(max_length=30)

    def __str__(self):
        return self.sname


class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    eeid=models.CharField(max_length=30)
    eaddr=models.CharField(max_length=60)

    def __str__(self):
        return self.ename



# Create your models here.
