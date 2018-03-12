from profile_matching.profiles.serializers.user import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
