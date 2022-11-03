from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import SportCrud
from rest_framework.response import Response
from .serializers import SportCrudSerializers

@api_view(
    ['GET', 'POST']
)
def sportcrud(request):
    if request.method == 'GET':
        sport = SportCrud.objects.all()
        serializer = SportCrudSerializers(sport, many=True)
        return Response(serializer.data)
    else:
        pass