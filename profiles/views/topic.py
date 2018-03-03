from profile_matching.profiles.models.topic import Topic
from profile_matching.profiles.serializers.topic import TopicSerializer
from rest_framework import generics
from rest_framework import permissions


class TopicList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
