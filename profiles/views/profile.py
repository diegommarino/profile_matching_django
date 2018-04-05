from profile_matching.profiles.models.profile import Profile
from profile_matching.profiles.serializers.profile import ProfileSerializer
from rest_framework import generics
from rest_framework import permissions
from profile_matching.profiles.permissions import IsOwnerOrReadOnly


class ProfileList(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
