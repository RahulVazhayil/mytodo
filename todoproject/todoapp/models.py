from django.db import models

# Create your models here.

class Task(models.Model):
    taskname=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()



    def __str__(self):
        return self.taskname
