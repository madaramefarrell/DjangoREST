from .. import serializers

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from ..models.beach import Beach
from rest_framework import status


class BeachListView(viewsets.ModelViewSet):

    # Use GET method "/api/beach"
    # Respond beach list information
    # Use GEt method with value "api/beach/?id=id"
    # Respond beach detail information

    def list(self, request, *args, **kwargs):
        postion = request.query_params.get('postion', None)
        if postion is None:
            queryset = get_list_or_404(Beach)
        else:
            queryset = get_list_or_404(Beach, location=postion)

        serialized = serializers.BeachListSerializer(queryset, many=True)
        return Response(serialized.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Beach, pk=pk)
        serialized = serializers.BeachDetailSerializer(queryset)
        return Response(serialized.data)

    def update(self, request, pk=None):
        queryset = Beach.objects.get(pk=pk)
        serialized = serializers.BeachDetailSerializer(queryset, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
