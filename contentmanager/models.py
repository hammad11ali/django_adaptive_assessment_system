from django.db import models

# Create your models here.


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """String"""
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        """String"""
        return self.name


class Concept(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    qgenerator = models.FileField(upload_to='Qgenerators/', null=True)

    def __str__(self):
        """String"""
        return self.name
