from .models import withDependents, withOutDependents, ZipMHA
from rest_framework import serializers

class withDependentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = withDependents
        fields = model._meta.get_all_field_names()