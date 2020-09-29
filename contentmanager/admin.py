from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Area)
admin.site.register(Topic)
admin.site.register(Concept)
admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(CourseEnrollment)
admin.site.register(AssessmentEnrollment)
admin.site.register(AsssessmentPerformance)
