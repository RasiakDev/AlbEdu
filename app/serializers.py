from rest_framework import serializers
from . import models

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parent
        fields = ('name', 'last_name')