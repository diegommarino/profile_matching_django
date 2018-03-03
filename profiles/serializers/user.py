from rest_framework import serializers
from django.contrib.auth.models import User
from profile_matching.profiles.models.profile import Profile


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'is_staff')
