from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    rollno=models.IntegerField()
    school=models.CharField(max_length=60)


    def __str__(self):
        return self.name

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    eaddr=models.CharField(max_length=60)
    emobno=models.IntegerField()

    def __str__(self):
        return self.ename

# Create your models here.
