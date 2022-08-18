from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import UserProfiles, Addresses
from .serializers import UserSerializer, UserProfileSerializer

@api_view(['GET', 'PUT','DELETE'])
def user_details(request, user_id):
    """
    Get, update, delete user details
    """
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['GET', 'PUT','DELETE'])
def user_profile(request, user_id):
    """
    Get, update, delete user profile details
    """
    if request.method == 'GET':
        user_profile = UserProfiles.objects.get(id=user_id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)