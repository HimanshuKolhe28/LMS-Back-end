
from django.urls import path
from library.views import BookViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', BookViewSet)


urlpatterns = router.urls
