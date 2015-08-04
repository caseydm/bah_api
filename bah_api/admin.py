from django.contrib import admin
from .models import withDependents, withOutDependents, ZipMHA

# Register your models here.
admin.site.register(withDependents)
admin.site.register(withOutDependents)
admin.site.register(ZipMHA)
