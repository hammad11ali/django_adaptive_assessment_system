from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Models


class UserProfileManager(BaseUserManager):
    """ Manager for user Profile"""

    def create_user(self, email, name, password=None, photo=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('No email provided')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        if photo:
            user.photo = photo
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password, photo=None):
        """Create new super User"""
        user = self.create_user(email, name, password, photo)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='photos/', height_field=None, width_field=None, max_length=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # password
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Full Name"""
        return self.name

    def get_short_name(self):
        """Short Name"""
        return self.name

    def __str__(self):
        """String"""
        return self.email

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

