from functools import partial
from urllib import request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.http import Http404

from .models import UserProfiles, Addresses, BlackListedToken
from .serializers import AddressesSerializer, UserSerializer, UserProfileSerializer
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
class UserDetailsView(APIView):
    """
    User details view
    """
    permission_classes = [IsAuthenticated, IsTokenValid]
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        serializer = UserSerializer(self.get_object(request.user.id))
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(instance=self.get_object(request.user.id), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        user = self.get_object(request.user.id)
        user.delete()
        token = (request.auth.token).decode('utf8')
        black_listed_token = BlackListedToken.objects.create(user=user, token=token)
        black_listed_token.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserProfilesView(APIView):
    """
    Get, update, delete user profile details
    """
    permission_classes = [IsAuthenticated, IsTokenValid]
    allowed_methods = ["GET"]
    def get_object(self, id):
        try:
            return UserProfiles.objects.get(user_id=id)
        except UserProfiles.DoesNotExist:
            raise Http404

    def get(self, request):
        serializer = UserProfileSerializer(self.get_object(request.user.id))
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserSerializer(instance=self.get_object(request.user.id), partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user_profile = self.get_object(request.user.id)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressView(APIView):
    permission_classes = (IsAuthenticated, IsTokenValid)
    allowed_methods = ['GET', 'POST']
    def get_object(self, id):
        try:
            return Addresses.objects.filter(user_profile__user=id)
        except Addresses.DoesNotExist:
            raise Http404
    def get(self, request):
        addresses = self.get_object(request.user.id)
        serializer = AddressesSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetailsView(APIView):
    permission_classes = (IsAuthenticated, IsTokenValid)
    allowed_methods = ['GET', 'PUT', 'DELETE']
    
    def get_object(self, pk):
        try:
            return Addresses.objects.get(pk=pk)
        except Addresses.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        serializer = AddressesSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        serializer = AddressesSerializer(instance=self.get_object(pk), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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