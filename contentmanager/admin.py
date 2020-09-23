from django.contrib import admin
from .models import Area
from .models import Topic
from .models import Concept
from .models import Course
from .models import Assessment
# Register your models here.

admin.site.register(Area)
admin.site.register(Topic)
admin.site.register(Concept)
admin.site.register(Course)
admin.site.register(Assessment)
