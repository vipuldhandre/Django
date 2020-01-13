from django.db import models

class Tech(models.Model):
    tnews=models.TextField()

    def __str__(self):
        return self.tnews

class Sports(models.Model):
    snews=models.TextField()

    def __str__(self):
        return self.snews

class Politics(models.Model):
    pnews=models.TextField()

    def __str__(self):
        return self.pnews


# Create your models here.
