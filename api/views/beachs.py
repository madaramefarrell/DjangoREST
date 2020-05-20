from ..models import beach
from .. import serializers

from rest_framework import viewsets
from rest_framework import mixins
from ..models.beach import Beach


class BeachListView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    def get_queryset(self):
        if self.action == 'list':
            queryset = Beach.objects.all()
        elif self.action == 'retrieve':
            pk = self.request.query_params.get('id', None)
            queryset = beach.Beach.objects.filter(id=pk)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BeachListSerializer
        elif self.action == 'detail':
            return serializers.BeachDetailSerializer
