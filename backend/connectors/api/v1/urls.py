from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135621ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135621", Testconnectors135621ViewSet, basename="testconnectors135621"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
