from .models import withDependents, withOutDependents, ZipMHA
from rest_framework import serializers

class withDependentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = withDependents
        fields = [
		'E1', 'E2','E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
		'W1', 'W2', 'W3', 'W4', 'W5', 'O1E', 'O2E', 'O3E', 'O1',
		'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'
		]