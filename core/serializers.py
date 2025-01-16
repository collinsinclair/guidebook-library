from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id", "first_name", "last_name", "website", "bio"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ["id", "name", "website"]


class GuidebookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = models.Guidebook
        fields = [
            "id",
            "title",
            "subtitle",
            "authors",
            "publisher",
            "edition",
            "year_published",
        ]


class TrailheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trailhead
        fields = ["id", "name", "latitude", "longitude", "elevation", "notes"]


class MountainRangeSerializer(serializers.ModelSerializer):
    subranges = serializers.SerializerMethodField()

    def get_subranges(self, obj):
        return MountainRangeSerializer(obj.subranges.all(), many=True).data

    class Meta:
        model = models.MountainRange
        fields = ["id", "name", "parent", "subranges"]


class PeakSerializer(serializers.ModelSerializer):
    mountain_range = MountainRangeSerializer(read_only=True)

    class Meta:
        model = models.Peak
        fields = [
            "id",
            "name",
            "latitude",
            "longitude",
            "elevation",
            "prominence",
            "isolation",
            "mountain_range",
        ]


class ColoradoSnowClimbsActivitySerializer(serializers.ModelSerializer):
    guidebook = GuidebookSerializer(read_only=True)
    trailhead = TrailheadSerializer(read_only=True)
    associated_peaks = PeakSerializer(many=True, read_only=True)
    snow_steepness_display = serializers.CharField(
        source="get_snow_steepness_display", read_only=True
    )
    in_season = serializers.BooleanField(source="is_in_season", read_only=True)

    class Meta:
        model = models.ColoradoSnowClimbsActivity
        fields = [
            "id",
            "name",
            "guidebook_number",
            "guidebook",
            "distance",
            "gain",
            "trailhead",
            "associated_peaks",
            "estimated_time_enroute",
            "yds_class",
            "season_bitmap",
            "season_text",
            "snow_steepness",
            "snow_steepness_display",
            "in_season",
        ]


class BestSummitHikesActivitySerializer(serializers.ModelSerializer):
    guidebook = GuidebookSerializer(read_only=True)
    trailhead = TrailheadSerializer(read_only=True)
    associated_peaks = PeakSerializer(many=True, read_only=True)
    crowd_level_display = serializers.CharField(
        source="get_crowd_level_display", read_only=True
    )
    in_season = serializers.BooleanField(source="is_in_season", read_only=True)

    class Meta:
        model = models.BestSummitHikesActivity
        fields = [
            "id",
            "name",
            "guidebook_number",
            "guidebook",
            "distance",
            "gain",
            "trailhead",
            "associated_peaks",
            "estimated_time_enroute",
            "yds_class",
            "season_bitmap",
            "season_text",
            "difficulty",
            "crowd_level",
            "crowd_level_display",
            "in_season",
        ]


class HikingColoradoActivitySerializer(serializers.ModelSerializer):
    guidebook = GuidebookSerializer(read_only=True)
    trailhead = TrailheadSerializer(read_only=True)
    associated_peaks = PeakSerializer(many=True, read_only=True)
    difficulty_display = serializers.CharField(
        source="get_difficulty_display", read_only=True
    )
    in_season = serializers.BooleanField(source="is_in_season", read_only=True)

    class Meta:
        model = models.HikingColoradoActivity
        fields = [
            "id",
            "name",
            "guidebook_number",
            "guidebook",
            "distance",
            "gain",
            "trailhead",
            "associated_peaks",
            "estimated_time_enroute",
            "yds_class",
            "season_bitmap",
            "season_text",
            "difficulty",
            "difficulty_display",
            "in_season",
        ]
