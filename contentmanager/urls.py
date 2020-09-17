from django.urls import path
from .views import *
urlpatterns = [
    path('concepts/', Concept_View.as_view()),
    path('topics/', Topic_View.as_view()),
    path('areas/', Area_View.as_view()),
]
