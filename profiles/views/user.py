from profile_matching.profiles.serializers.user import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer
