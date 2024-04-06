from django.shortcuts import render
from rest_framework import viewsets
from .models import Checkin
from .serializers import CheckinSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CheckinViewSet(viewsets.ModelViewSet):
  queryset = Checkin.objects.all().order_by('id')
  serializer_class = CheckinSerializer

  def list(self, request, *args, **kwargs):
    queryset = Checkin.objects.all()
    serializer = CheckinSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
  def create(self, request, *args, **kwargs):
    serializer = CheckinSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = CheckinSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)