from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 250)
    status = models.BooleanField(default = False)
