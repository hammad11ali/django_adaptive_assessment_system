from django.contrib import admin
from profiles_api import models
from .models import Area
from .models import Topic
from .models import Concept
# Register your models here.

admin.site.register(models.UserProfile)
# admin.site.register(Area)
# admin.site.register(Topic)
# admin.site.register(Concept)
