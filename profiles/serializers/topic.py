from rest_framework import serializers
from profile_matching.profiles.models.profile import Profile
from profile_matching.profiles.models.topic import Topic


class TopicSerializer(serializers.ModelSerializer):
    profiles = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())

    class Meta:
        model = Topic
        fields = ('id',
                  'name',
                  'profiles')
