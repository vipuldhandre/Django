from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=30)
    propic=models.ImageField(upload_to='media/')
    profile_created=models.DateTimeField(auto_now_add=True)
# Create your models here.
