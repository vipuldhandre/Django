from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30)
    srn = models.IntegerField()
    sclass = models.CharField(max_length=30)
    smarks = models.IntegerField()

    def __str__(self):
        return self.sname



# Create your models here.
