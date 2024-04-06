from django.shortcuts import render
from rest_framework import viewsets
from .models import Prompt
from .serializers import PromptSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from checkin.models import Checkin

class PromptViewSet(viewsets.ModelViewSet):
  queryset = Prompt.objects.all().order_by('text')
  serializer_class = PromptSerializer
  def list(self, request, *args, **kwargs):
    queryset = Prompt.objects.all()
    serializer = PromptSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
  def create(self, request, *args, **kwargs):
    serializer = PromptSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    date = serializer.data.get('date')
    prompt = Prompt.objects.get(date=date, text=serializer.data.get('text'))

    for user in User.objects.all():
      Checkin.objects.create(user=user, date=date, prompt=prompt)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = PromptSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)