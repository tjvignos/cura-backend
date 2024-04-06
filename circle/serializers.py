from rest_framework import serializers
from .models import Circle
from user.serializers import UserSerializer

class CircleSerializer(serializers.ModelSerializer):
  users = UserSerializer(many=True, read_only=True)
  class Meta:
      model = Circle
      fields = ['id', 'name', 'created_at', 'users']