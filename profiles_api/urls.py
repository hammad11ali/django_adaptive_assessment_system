from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
from .views import *
router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('user/', include(router.urls)),
    path('', include('contentmanager.urls')),
    path('concepts/', Concept_View.as_view()),
    path('topics/', Topic_View.as_view()),
    path('areas/', Area_View.as_view()),
]
