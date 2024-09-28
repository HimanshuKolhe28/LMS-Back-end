from django.contrib import admin 
from django.urls import path, include

from lms_backend.views import StudentViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),

] + router.urls



