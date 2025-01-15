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
