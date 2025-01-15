from django.contrib import admin

from core.forms import LocationFormBase
from core.models import Author, Guidebook, MountainRange, Peak, Publisher, Trailhead


class PeakAdminForm(LocationFormBase):
    class Meta:
        model = Peak
        fields = [
            "name",
            "latitude",
            "longitude",
            "elevation",
            "prominence",
            "isolation",
            "mountain_range",
        ]


class TrailheadAdminForm(LocationFormBase):
    class Meta:
        model = Trailhead
        fields = ["name", "latitude", "longitude", "elevation", "notes"]


@admin.register(Peak)
class PeakAdmin(admin.ModelAdmin):
    form = PeakAdminForm


@admin.register(Trailhead)
class TrailheadAdmin(admin.ModelAdmin):
    form = TrailheadAdminForm


models = [Author, Publisher, Guidebook, MountainRange]
for model in models:
    admin.site.register(model)
