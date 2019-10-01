from django.db import models

# Create your models here.

class List(models.Model):
    complete = models.BooleanField(default=False)
    listText = models.CharField(max_length=50)

    def __str__(self):
        return List.listText