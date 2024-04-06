from django.shortcuts import render
from rest_framework import viewsets
from .models import Circle
from .serializers import CircleSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.

class CircleViewSet(viewsets.ModelViewSet):
  queryset = Circle.objects.all().order_by('name')
  serializer_class = CircleSerializer

  def list(self, request, *args, **kwargs):
    queryset = Circle.objects.all()
    serializer = CircleSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
  def create(self, request, *args, **kwargs):
    serializer = CircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = CircleSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['POST'])
def add_user(request, pk, user_id):
  circle = Circle.objects.get(pk=pk)
  user = User.objects.get(pk=user_id)
  circle.users.add(user)
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def remove_user(request, pk, user_id):
  circle = Circle.objects.get(pk=pk)
  user = User.objects.get(pk=user_id)
  circle.users.remove(user)
  return Response(status=status.HTTP_204_NO_CONTENT)