from django.forms import CharField
#from django.shortcuts import render

from rest_framework import viewsets
from api import serializers
from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#class CheckboxViewSet(viewsets.ModelViewSet):
#    queryset = Checkbox.objects.all()
#    serializer_class = CheckboxSerializer

@api_view(['GET'])
def checkbox_list(req):
    checkboxes = Checkbox.objects.all()
    serializer = CheckboxSerializer(checkboxes, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox)
    except Checkbox.DoesNotExist:
        return Response (( f"error: Checkbox with id = {pk} is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['POST'])
def checkbox_create(req):
    serializer = CheckboxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist:
        return Response (( f"error: Checkbox with id = {pk} is not found"), status = status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

