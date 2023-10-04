from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Item
from .serializers import ItemSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    
   
 
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)

    return Response(serializer.data)
