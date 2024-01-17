from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ListingViewSet, AgentViewSet


router = SimpleRouter()
router.register("agents", AgentViewSet, basename="agents")
router.register("", ListingViewSet, basename="listings")

urlpatterns = router.urls
