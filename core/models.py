from django.db import models


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


class ActivityBaseClass(models.Model):
    name = models.CharField(max_length=64)
    guidebook_number = models.IntegerField(null=True, blank=True)
    guidebook = models.ForeignKey(
        Guidebook, related_name="activities", on_delete=models.PROTECT
    )
    distance = models.FloatField(help_text="Round-trip distance in miles.")
    gain = models.IntegerField(help_text="Total elevation gain in feet.")
    trailhead = models.ForeignKey(
        Trailhead, related_name="Activities", on_delete=models.PROTECT
    )
    associated_peaks = models.ManyToManyField(
        Peak, related_name="activities", blank=True
    )
    estimated_time_enroute = models.IntegerField(
        help_text="In minutes.", null=True, blank=True
    )
    yds_class = models.FloatField(
        help_text="Enter the highest grade in the case of multiple. Use .5 for +. e.g. 2/3+ -> 3.5.",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
