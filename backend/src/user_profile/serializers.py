from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfiles, Addresses

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)

class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    addresses = AddressesSerializer(many=True)
    class Meta:
        model = UserProfiles
        fields = '__all__'