from django.contrib import admin
from .models import withDependents, ZipMHA

# Register your models here.
admin.site.register(withDependents)
admin.site.register(ZipMHA)