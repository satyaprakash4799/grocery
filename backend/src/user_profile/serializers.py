from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfiles, Addresses

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = { 'password': {'write_only': True}}

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
        read_only_fields = ('id', 'user', 'addresses')