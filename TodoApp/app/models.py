from django.db import models

class Todoapp(models.Model):
    content=models.TextField()

    def __str__(self):
        return self.content




# Create your models here.
