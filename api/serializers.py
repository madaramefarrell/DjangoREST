from rest_framework import serializers
from .models import beach


class BeachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = beach.Beach
        field = ('__all__')
