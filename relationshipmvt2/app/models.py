from django.db import models

class Language(models.Model):
    lname=models.CharField(max_length=30)

    def __str__(self):
        return self.lname

class Framework(models.Model):
    fname=models.CharField(max_length=30)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname


class Movie(models.Model):
    mname=models.CharField(max_length=60)

    def __str__(self):
        return self.mname

class Actor(models.Model):
    aname=models.CharField(max_length=30)
    movie=models.ManyToManyField(Movie)
    
    def __str__(self):
        return self.aname

# Create your models here.
