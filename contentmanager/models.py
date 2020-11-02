from django.db import models
from profiles_api.models import UserProfile
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


class ConceptInCourse(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    totalQuestions = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)


class ConceptInAssessment(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)


class CourseEnrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class AssessmentEnrollment(models.Model):
    courseEnrollment = models.ForeignKey(
        CourseEnrollment, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    is_open= models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class AsssessmentPerformance(models.Model):
    assessmentEnrollment = models.ForeignKey(
        AssessmentEnrollment, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    performance = models.IntegerField()

    class Meta:
        ordering = ['-performance']
