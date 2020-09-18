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


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        """String"""
        return self.name

    def __str__(self):
        """String"""
        return self.description
class Chapter(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    position=models.IntegerField()

    def __str__(self):
        """String"""
        return self.name

    def __str__(self):
        """String"""
        return self.description

class ConceptInChapter(models.Model):
    chapterid=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    conceptid=models.ForeignKey(Concept,on_delete=models.CASCADE)
    position=models.IntegerField()

