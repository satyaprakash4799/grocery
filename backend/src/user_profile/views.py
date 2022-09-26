from functools import partial
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import UserProfiles, Addresses, BlackListedToken
from .serializers import UserSerializer, UserProfileSerializer
from .permissions import IsTokenValid, IsNotAuthenticated

@api_view(['POST'])
@permission_classes([IsNotAuthenticated])
def create_user(request):
    """Create a new user"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated, IsTokenValid])
def user_details(request):
    """
    Get, update, delete user details
    """
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
@permission_classes([IsAuthenticated, IsTokenValid])
def user_profile(request):
    """
    Get, update, delete user profile details
    """
    try:
        user_profile = UserProfiles.objects.get(user_id=request.user.id)
    except UserProfiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsTokenValid])
def logout(request):
    if request.method == 'POST':
        try:
            user = request.user
            token = (request.auth.token).decode('utf8')
            black_listed_token = BlackListedToken.objects.create(user=user, token=token)
            black_listed_token.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(e)