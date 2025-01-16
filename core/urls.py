from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"authors", views.AuthorViewSet)
router.register(r"publishers", views.PublisherViewSet)
router.register(r"guidebooks", views.GuidebookViewSet)
router.register(r"trailheads", views.TrailheadViewSet)
router.register(r"mountain-ranges", views.MountainRangeViewSet)
router.register(r"peaks", views.PeakViewSet)
router.register(r"colorado-snow-climbs", views.ColoradoSnowClimbsActivityViewSet)
router.register(r"best-summit-hikes", views.BestSummitHikesActivityViewSet)
router.register(r"hiking-colorado", views.HikingColoradoActivityViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
