from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.event_name

class Remember(models.Model):
    name=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Document(models.Model):
    name=models.CharField(max_length=100)
    doc=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Task(models.Model):
    name=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name

class Day_task(models.Model):
    day=models.IntegerField(null=True)
    month=models.IntegerField(null=True)
    year=models.IntegerField(null=True)
    tasks=models.ManyToManyField('Task',null=True)