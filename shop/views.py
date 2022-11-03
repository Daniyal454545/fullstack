from rest_framework import response, permissions
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import Shop
from rest_framework.response import Response
from .serializers import ShopSerializers
from . import serializers



class ShopViewSet(ModelViewSet):

    queryset = Shop.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ShopSerializers


    def get_permissions(self):
        if self.action in (
            'update',
            'partial_update',
            'destroy'
        ):
            pass

    def perfom_create(self, serializer):
        serializer.save(owner=self.request.user)



    @api_view(
        ['GET', 'POST']
    )
    def shopview(self, request, pk):
        shop = self.get_object()
        if request.method == 'GET':
            rs = shop.shopview.all()
            serializer = ShopSerializers(rs, many=True)
            return response.Response(serializer.data, status=200)
        elif request.method == 'POST':
            # current_shop = request.
            pass