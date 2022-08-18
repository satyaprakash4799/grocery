from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'