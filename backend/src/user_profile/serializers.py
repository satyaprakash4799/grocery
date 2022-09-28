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
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = { 'password': {'write_only': True}}

class AddressesSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        instance.user_profile = validated_data.get('user_profile', instance.user_profile)
        instance.apartment_name = validated_data.get('apartment_name', instance.apartment_name)
        instance.street_details = validated_data.get('street_details', instance.street_details)
        instance.landmark_details = validated_data.get('landmark_details', instance.landmark_details)
        instance.area_details = validated_data.get('area_details', instance.area_details)
        instance.city = validated_data.get('city', instance.city)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.save()
        return instance
    class Meta:
        model = Addresses
        fields = '__all__'
        read_only_fields = ('id',)

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    addresses = AddressesSerializer(many=True)
    
    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance
    class Meta:
        model = UserProfiles
        fields = '__all__'
        read_only_fields = ('addresses','user_profile')
        # extra_kwargs = { 'user': {'write_only': True}}