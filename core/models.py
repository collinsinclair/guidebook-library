from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=64)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Guidebook(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128, null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name="guidebooks")
    publisher = models.ForeignKey(
        Publisher, related_name="publications", on_delete=models.PROTECT
    )
    edition = models.IntegerField()
    year_published = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.edition}ed ({self.year_published})"


class Location(models.Model):
    latitude = models.FloatField(help_text="Use - for southern latitudes.")
    longitude = models.FloatField(help_text="Use - for western longitudes.")
    elevation = models.IntegerField(help_text="Elevation in feet.")

    class Meta:
        abstract = True

    def __str__(self):
        return f"({self.latitude:.3f}, {self.longitude:.3f})"


class Trailhead(Location):
    name = models.CharField(max_length=64)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.elevation:,} ft)"


class MountainRange(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="subranges",
    )

    def __str__(self):
        return f"{self.name}"


class Peak(Location):
    name = models.CharField(max_length=64)
    prominence = models.IntegerField(help_text="In feet.")
    isolation = models.FloatField(help_text="In miles.")
    mountain_range = models.ForeignKey(MountainRange, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"


def validate_binary_string(value):
    if len(value) != 12:
        raise ValidationError("Season bitmap must be exactly 12 digits long")

    if not all(char in "01" for char in value):
        raise ValidationError("Season bitmap can only contain 0s and 1s")


class ActivityBaseClass(models.Model):
    name = models.CharField(max_length=64)
    guidebook_number = models.IntegerField(null=True, blank=True)
    guidebook = models.ForeignKey(
        Guidebook, related_name="%(class)s_activities", on_delete=models.PROTECT
    )
    distance = models.FloatField(help_text="Round-trip distance in miles.")
    gain = models.IntegerField(help_text="Total elevation gain in feet.")
    trailhead = models.ForeignKey(
        Trailhead, related_name="%(class)s_activities", on_delete=models.PROTECT
    )
    associated_peaks = models.ManyToManyField(
        Peak, related_name="%(class)s_activities", blank=True
    )
    estimated_time_enroute = models.IntegerField(
        help_text="In minutes.", null=True, blank=True
    )
    yds_class = models.FloatField(
        help_text="Enter the highest grade in the case of multiple. Use .5 for +. e.g. 2/3+ -> 3.5.",
        null=True,
        blank=True,
    )
    season_bitmap = models.CharField(
        max_length=12, validators=[validate_binary_string], null=True, blank=True
    )
    season_text = models.CharField(max_length=128, null=True, blank=True)

    def is_in_season(self):
        if not self.season_bitmap:
            return False
        current_month = timezone.now().month
        bitmap_int = int(self.season_bitmap, 2)
        return bool(bitmap_int & (1 << (12 - current_month)))

    class Meta:
        abstract = True


SNOW_STEEPNESS_CHOICES = {
    "EA": "Easy (0-30 degrees)",
    "MO": "Moderate (30-45 degrees)",
    "ST": "Steep (45-60 degrees)",
    "VS": "Very Steep (60-80 degrees)",
    "VE": "Vertical (80-90 degrees)",
}


class ColoradoSnowClimbsActivity(ActivityBaseClass):
    snow_steepness = models.CharField(
        max_length=2,
        choices=SNOW_STEEPNESS_CHOICES,
        help_text="Enter the steepest listed.",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Colorado Snow Climbs Activity"
        verbose_name_plural = "Colorado Snow Climbs Activities"


CROWD_LEVEL_CHOICES = {"HE": "Hermit", "LO": "Low", "MO": "Moderate", "HI": "High"}


class BestSummitHikesActivity(ActivityBaseClass):
    difficulty = models.FloatField()
    crowd_level = models.CharField(
        max_length=2,
        help_text="Enter the lowest crowd level.",
        choices=CROWD_LEVEL_CHOICES,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Best Summit Hikes Activity"
        verbose_name_plural = "Best Summit Hikes Activities"
