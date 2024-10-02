from django.db import models

# Create your models here.
class Todolist(models.Model):
    task = models.TextField()
    deline = models.TimeField()
    prio = models.IntegerField(null=True)