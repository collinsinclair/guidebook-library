from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class BaseReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []


class AuthorViewSet(BaseReadOnlyViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class PublisherViewSet(BaseReadOnlyViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer


class GuidebookViewSet(BaseReadOnlyViewSet):
    queryset = models.Guidebook.objects.all()
    serializer_class = serializers.GuidebookSerializer


class TrailheadViewSet(BaseReadOnlyViewSet):
    queryset = models.Trailhead.objects.all()
    serializer_class = serializers.TrailheadSerializer


class MountainRangeViewSet(BaseReadOnlyViewSet):
    queryset = models.MountainRange.objects.all()
    serializer_class = serializers.MountainRangeSerializer


class PeakViewSet(BaseReadOnlyViewSet):
    queryset = models.Peak.objects.all()
    serializer_class = serializers.PeakSerializer


class ColoradoSnowClimbsActivityViewSet(BaseReadOnlyViewSet):
    queryset = models.ColoradoSnowClimbsActivity.objects.all()
    serializer_class = serializers.ColoradoSnowClimbsActivitySerializer


class BestSummitHikesActivityViewSet(BaseReadOnlyViewSet):
    queryset = models.BestSummitHikesActivity.objects.all()
    serializer_class = serializers.BestSummitHikesActivitySerializer


class HikingColoradoActivityViewSet(BaseReadOnlyViewSet):
    queryset = models.HikingColoradoActivity.objects.all()
    serializer_class = serializers.HikingColoradoActivitySerializer
