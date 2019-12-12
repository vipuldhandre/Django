from django.db import models

class Employee(models.Model):
    eid = models.PositiveIntegerField(primary_key=True,null=False,blank=False)
    ename = models.CharField(max_length=30,blank=False,null=False)
    edes = models.CharField(max_length=30,blank=False,null=False)
    esal = models.FloatField(blank=False,null=False)

    def __str__(self):
        return self.ename

    class Meta:
        db_table = 'employee'
