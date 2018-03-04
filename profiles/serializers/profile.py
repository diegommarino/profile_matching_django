from rest_framework import serializers
from profile_matching.profiles.models.profile import Profile
from profile_matching.profiles.models.topic import Topic


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=Topic.objects.all())

    class Meta:
        model = Profile
        fields = ('id',
                  'first_name',
                  'last_name',
                  'current_position',
                  'avatar',
                  'about',
                  'topics',
                  'owner')
