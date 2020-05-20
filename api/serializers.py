from rest_framework import serializers
from .models import beach

class BeachListSerializer(serializers.ModelSerializer):
    class Meta:
        model = beach.Beach
        fields = ['id', 'name']

class BeachDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="beach_status")

    class Meta:
        model = beach.Beach
        fields = ['id', 'name', 'location', 'lat', 'lng', 'status']



