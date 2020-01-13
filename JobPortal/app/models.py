from django.db import models


class Engineering(models.Model):
    ejobs = models.TextField()

    def __str__(self):
        return self.ejobs

class Management(models.Model):
    mjobs = models.TextField()

    def __str__(self):
        return self.mjobs

class Operations(models.Model):
    ojobs = models.TextField()

    def __str__(self):
        return self.ojobs
# Create your models here.
