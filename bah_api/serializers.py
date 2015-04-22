from .models import withDependents, withOutDependents, ZipMHA
from rest_framework import serializers

class withDependentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = withDependents
        fields = ('MHA', 'E1', 'E2', 'E3')