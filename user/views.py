from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from checkin.models import Checkin
from .serializers import UserSerializer
from circle.serializers import CircleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from zoneinfo import ZoneInfo
from prompt.models import Prompt
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('username')
  serializer_class = UserSerializer

  def list(self, request, *args, **kwargs):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
  def create(self, request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    date = datetime.now(ZoneInfo('America/New_York')).date()
    user = User.objects.get(username=request.data.get('username'))
    for prompt in Prompt.objects.all():
      if prompt.date >= date:
        Checkin.objects.create(user=user, prompt=prompt, date=prompt.date)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = UserSerializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register(request):
  serializer = UserSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  user = User.objects.get(username=request.data.get('username'))

  date = datetime.now(ZoneInfo('America/New_York')).date()
  for prompt in Prompt.objects.all():
    if prompt.date >= date:
      Checkin.objects.create(user=user, prompt=prompt, date=prompt.date)

  user.set_password(request.data.get('password'))
  user.save()
  token = Token.objects.create(user=user)

  return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
  
@api_view(['POST'])
def login(request):
  user = get_object_or_404(User, username=request.data.get('username'))
  if not user.check_password(request.data.get('password')):
    return Response(status=status.HTTP_401_UNAUTHORIZED)
  token, created = Token.objects.get_or_create(user=user)
  serializer = UserSerializer(user)
  return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
  return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def checkin(request, pk):
  user = User.objects.get(pk=pk)
  date = datetime.now(ZoneInfo('America/New_York')).date()
  checkin = Checkin.objects.get(user=user, date=date)
  checkin.checked = True
  if 'response' in request.data:
    checkin.response = request.data.get('response')
  checkin.save()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def circles(request, pk):
  user = User.objects.get(pk=pk)
  circles = user.circles.all()
  serializer = CircleSerializer(circles, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def mutualcircles(request, pk, sk):
  user1 = User.objects.get(pk=pk)
  user2 = User.objects.get(pk=sk)
  user1_circles = user1.circles.all()
  user2_circles = user2.circles.all()
  circles = []
  for circle in user1_circles:
    if circle in user2_circles:
      circles.append(circle)
  serializer = CircleSerializer(circles, many=True)
  return Response(serializer.data)