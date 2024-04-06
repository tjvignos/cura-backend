from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  circles = serializers.StringRelatedField(many=True, read_only=True)
  class Meta:
      model = User
      fields = ['id', 'username', 'password', 'circles']