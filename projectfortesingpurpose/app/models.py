from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateTimeField(auto_now_add=False)

    class Meta:
        managed = True
        db_table = "test"

    def __str__(self):
        return self.name
