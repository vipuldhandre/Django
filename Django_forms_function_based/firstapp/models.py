from django.db import models


class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=30)
    edes = models.CharField(max_length=30)
    esal = models.FloatField()


    def __str__(self):
        return self.ename


    class Meta:
        db_table = 'employee'
# Create your models here.
