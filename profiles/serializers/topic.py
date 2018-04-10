from rest_framework import serializers
from profiles.models.profile import Profile
from profiles.models.topic import Topic


class TopicSerializer(serializers.ModelSerializer):
    profiles = serializers.ReadOnlyField()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'profiles')
