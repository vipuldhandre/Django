from django.db import models

# Create your models here.
class Stusearch(models.Model):
    stuname=models.CharField(max_length=30)

    def __str__(self):
        return self.stuname
        
