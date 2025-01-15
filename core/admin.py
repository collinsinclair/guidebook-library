from django.contrib import admin

from core.models import Author, Guidebook, Publisher

models = [Author, Publisher, Guidebook]

for model in models:
    admin.site.register(model)
