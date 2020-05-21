from .. import serializers

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ..models.beach import Beach


class BeachListView(viewsets.ReadOnlyModelViewSet):


    def get_queryset(self):
        queryset = get_list_or_404(Beach)
        return queryset
    def get_serializer_class(self):
        serializer_class = serializers.BeachListSerializer
        return serializer_class

    # Use GET method "/api/beach"
    # Respond beach list information
    # Use GEt method with value "api/beach/?id=id"
    # Respond beach detail information

    def list(self, request, *args, **kwargs):
        id = request.query_params.get('id', None)
        queryset = self.get_queryset()

        if id is not None:
            queryset = get_list_or_404(Beach, id=id)
            serialized_data = serializers.BeachDetailSerializer(queryset, many=True)
        else:
            serialized_data = self.get_serializer(queryset, many=True)

        return Response(serialized_data.data)
