from rest_framework import serializers
from profile_matching.profiles.models.profile import Profile
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'profile', 'is_staff')
