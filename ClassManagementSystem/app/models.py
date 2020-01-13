from django.db import models

class Course(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(self):
        return self.cname

class Faculty(models.Model):
    fname=models.CharField(max_length=30)

    def __str__(self):
        return self.fname

class Batch(models.Model):
    bname=models.CharField(max_length=30)

    def __str__(self):
        return self.bname

class Student(models.Model):
    sname=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ManyToManyField(Faculty)
    batch=models.ManyToManyField(Batch)

    def __str__(self):
        return self.sname
# Create your models here.
