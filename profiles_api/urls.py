from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('user/', include(router.urls)),
]
