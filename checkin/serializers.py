from rest_framework import serializers
from .models import Checkin

class CheckinSerializer(serializers.ModelSerializer):
  class Meta:
      model = Checkin
      fields = ['id', 'user', 'prompt', 'date', 'checked', 'response']