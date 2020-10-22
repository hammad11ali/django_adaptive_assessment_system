from django.urls import path
from .views import *
urlpatterns = [
    path('concepts/', Concept_View.as_view()),
    path('topics/', Topic_View.as_view()),
    path('areas/', Area_View.as_view()),
    path('quiz/', Quiz_View.as_view()),
    path('courses/', Course_View.as_view()),
    path("conceptincourse/", ConceptInCourse_View.as_view()),
    path('assessments/', Assessment_View.as_view()),
    path('conceptinassessment/', ConceptInAssessment_View.as_view()),
    path('courseEnrollment/', CourseEnrollment_View.as_view()),
    path('assessmentenrollment/', AssessmentEnroll_View.as_view()),
    path('performance/', Performance_View.as_view()),
]
